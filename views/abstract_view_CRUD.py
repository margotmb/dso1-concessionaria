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

    def lista(self, titulo : str, lista_objetos: list, lista_info: list, num_info: int):
        layout = [
                [sg.Output(size=(40,30), key="_output_")],
                [sg.Button('Listar'),sg.Button('Limpar')],
                [sg.Text('Busca ID:'), sg.InputText(size=(21,1)), sg.Button('Buscar')],
                [sg.Button('Voltar')]
        ]  
        window = sg.Window(titulo).Layout(layout)
        button, values = window.Read(timeout=5)

        #Loop da Janela
        while button != 'Voltar':

            #Printa a lista
            window.FindElement('_output_').Update('')
            for j in lista_info:
                print(j)

            #Limpa Lista
            if button == 'Limpar':
                window.FindElement('_output_').Update('')
            
            #Busca por ID
            if button == 'Buscar':
                lista = []
                try:
                    numero = int(values[0])
                except ValueError as e:
                    sg.popup('\nERRO: Input inválido')
                try:
                    for obj in lista_objetos:
                        if obj.num_id == numero:
                            posicao = lista_info.index("ID: " + str(obj.num_id))
                            for i in range(posicao, posicao+num_info):
                                lista.append(lista_info[i])
                            window.FindElement('_output_').Update('')
                            for j in lista:
                                print(j)
                except Exception as e:
                    sg.popup('ERRO:{}'.format(e))
                
                if lista == []:
                    sg.popup("Vendedor não encontrado")
                
            #Lê o próximo input
            button, values = window.Read()
        #Fecha janela ao sair do loop
        window.close()

    def tela_input_id(self, lista_info, titulo):
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
            for j in lista_info:
                print(j)

            #Enviar ID
            button, values = window.Read()
            if button == 'Submit':
                try:
                    values[0] = int(values[0])
                except ValueError:
                    self.erro('\nERRO: Dado Inválido')
                    window.close()
                    return None
                else:
                    window.close()
                    return values[0]

        window.close()
    
    def sucesso(self):
        sg.popup("Operação realizada com sucesso",  line_width=20)
    
    def erro(self, mensagem_erro: str):
        sg.popup("\n" + mensagem_erro)