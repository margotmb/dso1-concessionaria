import os
import PySimpleGUI as sg
from views.abstract_view_CRUD import AbstractViewCRUD

class VendedorView(AbstractViewCRUD):
    def __init__(self):
        pass

    def tela_principal(self):
        layout = [
            [sg.Text("---- VENDEDORES ----", justification='center',size=(20,1))],
            [sg.Button(button_text="1"), sg.Text(" <- Cadastrar")],
            [sg.Button(button_text="2"), sg.Text(" <- Listar")],
            [sg.Button(button_text="3"), sg.Text(" <- Atualizar")],
            [sg.Button(button_text="4"), sg.Text(" <- Remover")],
            [sg.Button(button_text="0"), sg.Text(" <- Sair")]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button,values = window.read()
        print(button, values)
        window.close()
        return button

    def cadastra(self):
        layout = [
                [sg.Text("Informações do Vendedor:")],
                [sg.Text('ID: ', size=(18,1)), sg.InputText()],
                [sg.Text('Nome: ', size=(18, 1)), sg.InputText()],
                [sg.Text('Telefone: ', size=(18, 1)), sg.InputText()],
                [sg.Submit(),sg.Button('Voltar')]
        ]
        return super().cadastra(layout, "Novo Vendedor")

    def lista(self, vendedores: list):
        lista_info = self.gera_lista_info(vendedores)
        super().lista('LISTAGEM DE VENDEDORES', vendedores, lista_info, 5)
        
    def vendedor_id(self, vendedores: list):
        lista = self.gera_lista_info(vendedores)
        return super().tela_input_id(lista, "ATUALIZAÇÃO DE VENDEDOR")

    def atualiza(self, nome: str, telefone: str):
        layout = [
            [sg.Text("Atualização de Vendedor", justification='center',size=(30,1), font='Courier 15', background_color='pink')],
            [sg.Text("Nome: "), sg.InputText(default_text=nome, size=(21,1))],
            [sg.Text("Telefone: "), sg.InputText(default_text=telefone, size=(21,1))],
            [sg.Button('Submit'), sg.Button('Voltar')]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        values = window.read()
        #num_id = self.vendedor_id(list(self.))
        window.close()
        return values

    def remove(self, vendedores: list):
        lista = self.gera_lista_info(vendedores)
        return super().tela_input_id(lista, "REMOÇÃO DE VENDEDOR")

    def gera_lista_info(self, vendedores):
        lista = []
        for item in vendedores:
            num_id = "ID: " + str(item.num_id)
            nome = "Nome: " + item.nome
            telefone = "Telefone: " + item.telefone
            carros_vendidos = "Carros Vendidos: " + str(item.carros_vendidos)
            receita_gerada = "Receita Gerada: R$" + str(item.receita_gerada)
            lista.extend([num_id,nome,telefone,carros_vendidos,receita_gerada, "\n"])
        
        return lista

