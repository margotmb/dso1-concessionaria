import os
import PySimpleGUI as sg


class ConcessionariaView:

    def __init__(self):
        pass

    def tela_principal(self, nome, endereco, cnpj):
        sg.theme('Purple')
        layout = [
            [sg.Text("Concessionária " + nome, justification='center',size=(25,1), font='Courier 15', background_color='pink', relief='sunken')],
            [sg.Button(button_text="1", size=(9,3)), sg.Text(" <- Gerenciamento")],
            [sg.Button(button_text="2", size=(9,3)), sg.Text(" <- Venda")],
            [sg.Button(button_text="3", size=(9,3)), sg.Text(" <- Relatorio")],
            #[sg.Button(button_text="4", size=(9,3)), sg.Text(" <- Concessionaria")],
            [sg.Button(button_text="0", size=(9,3)), sg.Text(" <- Sair")],
            [sg.Text("Endereço: " + endereco, size=(40,1), justification='right', font='Courier 10', background_color='pink', pad=((3, 0),(50,0)))],
            [sg.Text("CNPJ: " + cnpj, size=(40,1), justification='right', font='Courier 10', background_color='pink',pad=((3, 0),(0,0)))]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button = window.read()[0]
        print(button)
        window.close()
        return button


    def tela_gerenciamento(self):
        layout = [
            [sg.Text("Gerenciamento", justification='center',size=(30,1), font='Courier 15', background_color='pink')],
            [sg.Button(button_text="1", size=(9,3)), sg.Text(" <- Vendedores")],
            [sg.Button(button_text="2", size=(9,3)), sg.Text(" <- Clientes"), ],
            [sg.Button(button_text="3", size=(9,3)), sg.Text(" <- Carros"), ],
            [sg.Button(button_text="0", size=(9,3)), sg.Text(" <- Voltar")]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button,values = window.read()
        print(button, values)
        window.close()
        return button
    
    # def tela_edicao(self, nome, endereco, cnpj):
    #     layout = [
    #         [sg.Text("Gerenciamento", justification='center',size=(30,1), font='Courier 15', background_color='pink')],
    #         [sg.Text("Nome: "), sg.InputText(default_text=nome, size=(21,1))],
    #         [sg.Text("Endereço: "), sg.InputText(default_text=endereco, size=(21,1))],
    #         [sg.Text("CNPJ: "), sg.InputText(default_text=cnpj, size=(21,1))],
    #         [sg.Button('Submit'), sg.Button('Voltar')]
    #     ]
    #     window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
    #     values = window.read()[1]
    #     window.close()
    #     return values