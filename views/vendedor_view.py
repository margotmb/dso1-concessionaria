import os
import PySimpleGUI as sg
from views.abstract_view_CRUD import AbstractViewCRUD

class VendedorView(AbstractViewCRUD):
    def __init__(self):
        pass

    def tela_principal(self):
        layout = [
            [sg.Text("---- VENDEDORES ----", justification='center',size=(20,1), font='Courier 15', background_color='pink')],
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
                [sg.Text("Informações do Vendedor:")],
                [sg.Text('ID: ', size=(18,1)), sg.InputText(size=(5,1))],
                [sg.Text('Nome: ', size=(18, 1)), sg.InputText()],
                [sg.Text('Telefone: ', size=(18, 1)), sg.InputText()],
                [sg.Submit(),sg.Button('Voltar')]
        ]
        return super().cadastra(layout, "Novo Vendedor")

    def lista(self, vendedores: list):
        layout = [
                [sg.Output(size=(40,30), key="_output_")],
                [sg.Button('Listar'), sg.Button('Voltar')],
        ]  
        window = sg.Window('Listagem - Vendedores').Layout(layout)
        button = window.Read(timeout=5)

        #Loop da Janela
        while button[0] != 'Voltar':
            lista = []
            for item in vendedores:
                num_id = "ID: " + str(item.num_id)
                nome = "Nome: " + item.nome
                telefone = "Telefone: " + item.telefone
                carros_vendidos = "Carros Vendidos: " + str(item.carros_vendidos)
                receita_gerada = "Receita Gerada: R$ " + str(item.receita_gerada)
                lista.extend([num_id,nome,telefone, carros_vendidos, receita_gerada, "\n"])

            window.FindElement('_output_').Update('')
            for j in lista:
                print(j)

            button = window.Read()
        window.close()
    
    def gera_lista_dados(self, vendedores):
        lista = []
        for item in vendedores:
            num_id = "ID: " + str(item.num_id)
            nome = "Nome: " + item.nome
            telefone = "Telefone: " + item.telefone
            carros_vendidos = "Carros Vendidos: " + str(item.carros_vendidos)
            receita_gerada = "Receita Gerada: R$" + str(item.receita_gerada)
            lista.extend([num_id,nome,telefone,carros_vendidos,receita_gerada, "\n"])
        
        return lista

    def vendedor_id(self, vendedores: list):
        lista = self.gera_lista_dados(vendedores)
        return super().tela_input_id(lista, "ATUALIZAÇÃO DE VENDEDOR")

    def atualiza(self, nome: str, telefone: str, num_id: int):
        layout = [
            [sg.Text("Atualização de Vendedor", justification='center',size=(30,1), font='Courier 15', background_color='pink')],
            [sg.Text("ID: " + str(num_id), background_color='pink')],
            [sg.Text("Nome: "), sg.InputText(default_text=nome, size=(21,1))],
            [sg.Text("Telefone: "), sg.InputText(default_text=telefone, size=(21,1))],
            [sg.Button('Submit'), sg.Button('Voltar')]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        button, values = window.read()
        window.close()
        if button == "Submit":
            return values
        else:
            return None

    def remove(self, vendedores: list):
        lista = self.gera_lista_dados(vendedores)
        return super().tela_input_id(lista, "REMOÇÃO DE VENDEDOR")
