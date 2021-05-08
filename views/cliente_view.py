import PySimpleGUI as sg
from views.abstract_view_CRUD import AbstractViewCRUD


class ClienteView(AbstractViewCRUD):
    def __init__(self):
        pass

    def tela_principal(self):
        layout = [
            [sg.Text("----Clientes----", justification='center', size=(20,1), font='Courier 15', background_color='pink')],
            [sg.Button(button_text="Cadastrar", font='Courier 12', size=(23,3))],
            [sg.Button(button_text="Listar", font='Courier 12', size=(23,3))],
            [sg.Button(button_text="Atualizar", font='Courier 12', size=(23,3))],
            [sg.Button(button_text="Remover", font='Courier 12', size=(23,3))],
            [sg.Button(button_text="Voltar", font='Courier 12', size=(23,3))]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        values = window.read()
        window.close()
        return values[0]

    def cadastra(self):
        layout = [
                [sg.Text("Informações do Cliente:")],
                [sg.Text('ID: ', size=(18,1)), sg.InputText(size=(5,1))],
                [sg.Text('Nome: ', size=(18, 1)), sg.InputText()],
                [sg.Text('Telefone: ', size=(18, 1)), sg.InputText()],
                [sg.Submit(),sg.Button('Voltar')]
        ]
        return super().cadastra(layout, "Novo Cliente")

    def lista(self, clientes: list):
        layout = [
                [sg.Output(size=(40,30), key="_output_")],
                [sg.Button('Listar'), sg.Button('Voltar')],
                
        ]  
        window = sg.Window('Listagem - Cliente').Layout(layout)
        button = window.Read(timeout=5)

        #Loop da Janela
        while button[0] != 'Voltar':
            lista = []
            for item in clientes:
                num_id = "ID: " + str(item.num_id)
                nome = "Nome: " + item.nome
                telefone = "Telefone: " + item.telefone
                lista.extend([num_id,nome,telefone, "\n"])

            #Printa a lista
            window.FindElement('_output_').Update('')
            for j in lista:
                print(j)

            #Lê o próximo input
            button = window.Read()
        #Fecha janela ao sair do loop
        window.close()

    def gera_lista_dados(self, clientes):
        lista = []
        for item in clientes:
            num_id = "ID: " + str(item.num_id)
            nome = "Nome: " + item.nome
            telefone = "Telefone: " + item.telefone
            lista.extend([num_id,nome,telefone, "\n"])
        
        return lista

    def cliente_id(self, clientes: list):
        lista = self.gera_lista_dados(clientes)
        return super().tela_input_id(lista, "ATUALIZAÇÃO DE CLIENTES")

    def atualiza(self, nome: str, telefone: str, num_id: int):
        layout = [
            [sg.Text("Atualização de Cliente", justification='center',size=(30,1), font='Courier 15', background_color='pink')],
            [sg.Text("ID: " + str(num_id), background_color='pink')],
            [sg.Text("Nome: "), sg.InputText(default_text=nome, size=(21,1))],
            [sg.Text("Telefone: "), sg.InputText(default_text=telefone, size=(21,1))],
            [sg.Button('Submit'), sg.Button('Voltar')]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        button,values = window.read()
        window.close()
        if button == "Submit":
            return values
        else:
            return None 

    def remove(self, clientes: list):
        lista = self.gera_lista_dados(clientes)
        return super().tela_input_id(lista, "REMOÇÃO DE CLIENTE")
