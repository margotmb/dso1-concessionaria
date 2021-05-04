import os
import PySimpleGUI as sg


class ConcessionariaView:

    def __init__(self):
        pass

    def tela_principal(self):
        sg.theme('Purple')
        layout = [
            [sg.Text("----Concessionária----", justification='center',size=(40,1))],
            [sg.Button(button_text="1"), sg.Text(" <- Gerenciamento")],
            [sg.Button(button_text="2"), sg.Text(" <- Venda"), ],
            [sg.Button(button_text="3"), sg.Text(" <- Relatorio"), ],
            [sg.Button(button_text="0"), sg.Text(" <- Sair")]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button,values = window.read()
        #print(button, values)
        window.close()
        return button


    def tela_gerenciamento(self):
        layout = [
            [sg.Text("----Gerenciamento----", justification='center',size=(20,1))],
            [sg.Button(button_text="1"), sg.Text(" <- Vendedores")],
            [sg.Button(button_text="2"), sg.Text(" <- Clientes"), ],
            [sg.Button(button_text="3"), sg.Text(" <- Carros"), ],
            [sg.Button(button_text="0"), sg.Text(" <- Voltar")]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button,values = window.read()
        print(button, values)
        window.close()
        return button
