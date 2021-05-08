from abc import ABC, abstractmethod
from models.vendedor import Vendedor
from models.cliente import Cliente
from models.carro import Carro
import PySimpleGUI as sg

class AbstractViewCRUD(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def cadastra(self, layout, titulo):
        window = sg.Window(titulo).Layout(layout)
        button, values = window.Read()
        
        #Envia cadastro
        if button == "Submit":
            try:
                values[0] = int(values[0])
            except ValueError as e:
                sg.popup('\nERRO: Caracter inválido: {}'.format(e))
                window.close()
                return None
            else:
                window.close()
                return values
        else:
            window.close()
            return None

    #Utilizado por Atualizar e Remover
    def tela_input_id(self, lista_dados, titulo):
        layout = [
                [sg.Output(size=(40,30), key="_output_")],
                [sg.Text('ID:'), sg.InputText(size=(21,1)),sg.Submit()],
                [sg.Button('Voltar')]
        ]
        window = sg.Window(titulo).Layout(layout)
        button, values = window.Read(timeout=5)

        #Loop da Janela
        while button != 'Voltar':

            #Listagem
            window.FindElement('_output_').Update('')
            for j in lista_dados:
                print(j)

            #Enviar ID
            button, values = window.Read()
            window.close()
            if button == 'Submit':
                try:
                    values[0] = int(values[0])
                except ValueError:
                    self.erro('\nERRO: ID Inválido')
                    return None
                else:
                    return values[0]
            else:
                return None

        window.close()
    
    def sucesso(self):
        sg.popup("Operação realizada com sucesso",  line_width=20)
    
    def erro(self, mensagem_erro: str):
        sg.popup("\n" + mensagem_erro)