import PySimpleGUI as sg
from views.abstract_view_CRUD import AbstractViewCRUD


class CarroView(AbstractViewCRUD):
    def __init__(self):
        pass

    def tela_principal(self):
        layout = [
            [sg.Text("----CARRO----", justification='center',size=(20,1), font='Courier 15', background_color='pink')],
            [sg.Button(button_text="1", size=(9,3)), sg.Text(" <- Cadastrar", font='Courier 12', background_color='pink')],
            [sg.Button(button_text="2", size=(9,3)), sg.Text(" <- Listar", font='Courier 12', background_color='pink')],
            [sg.Button(button_text="3", size=(9,3)), sg.Text(" <- Atualizar", font='Courier 12', background_color='pink')],
            [sg.Button(button_text="4", size=(9,3)), sg.Text(" <- Remover", font='Courier 12', background_color='pink')],
            [sg.Button(button_text="0", size=(9,3)), sg.Text(" <- Sair", font='Courier 12', background_color='pink')]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button = window.read()
        window.close()
        return button[0]

    def cadastra(self):
        layout = [
                [sg.Text("Informações do Carro:")],
                [sg.Text('ID: ', size=(18,1)), sg.InputText(size=(5,1))],
                [sg.Text('Marca: ', size=(18, 1)), sg.InputText()],
                [sg.Text('Modelo: ', size=(18, 1)), sg.InputText()],
                [sg.Text('Ano: ', size=(18, 1)), sg.InputText()],
                [sg.Text('Valor: R$ ', size=(18, 1)), sg.InputText()],
                [sg.Submit(),sg.Button('Voltar')]
        ]
        return super().cadastra(layout, "Novo Vendedor")

    def lista(self, carros: list):
        layout = [
                [sg.Output(size=(40,30), key="_output_")],
                [sg.Button('Listar'), sg.Button('Voltar')],
        ]  
        window = sg.Window('Listagem - Carros').Layout(layout)
        button = window.Read(timeout=5)

        #Loop da Janela
        while button[0] != 'Voltar':
            lista = []
            for item in carros:
                num_id = "ID: " + str(item.num_id)
                marca = "Marca: " + item.marca
                modelo = "Modelo: " + item.modelo
                ano = "Ano: " + item.ano
                valor = "Valor: R$" + item.valor
                lista.extend([num_id, marca, modelo, ano, valor, "\n"])

            window.FindElement('_output_').Update('')
            for j in lista:
                print(j)

            button = window.Read()
        window.close()

    def gera_lista_dados(self, carros: list):
        lista = []
        for item in carros:
            num_id = "ID: " + str(item.num_id)
            marca = "Marca: " + item.marca
            modelo = "Modelo: " + item.modelo
            ano = "Ano: " + item.ano
            valor = "Valor: R$" + item.valor
            lista.extend([num_id, marca, modelo, ano, valor, "\n"])

        return lista

    def carro_id(self, carros: list):
        lista = self.gera_lista_dados(carros)
        return super().tela_input_id(lista, "ATUALIZAÇÃO DE CARRO")

    def atualiza(self, marca, modelo, ano, valor, num_id):
        layout = [
            [sg.Text("Atualização de Carro", justification='center',size=(30,1), font='Courier 15', background_color='pink')],
            [sg.Text("ID: " + str(num_id), background_color='pink')],
            [sg.Text("Marca: "), sg.InputText(default_text=marca, size=(21,1))],
            [sg.Text("Modelo: "), sg.InputText(default_text=modelo, size=(21,1))],
            [sg.Text("Ano: "), sg.InputText(default_text=str(ano), size=(21,1))],
            [sg.Text("Valor: R$ "), sg.InputText(default_text=str(valor), size=(21,1))],
            [sg.Button('Submit'), sg.Button('Voltar')]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        button, values = window.read()
        window.close()
        if button == "Submit":
            return values
        else:
            return None

    def remove(self, carros: list):
        lista = self.gera_lista_dados(carros)
        return super().tela_input_id(lista, "REMOÇÃO DE CARRO")
