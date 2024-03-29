import PySimpleGUI as sg


class MainView:
    def __init__(self):
        pass

    def tela_principal(self):
        sg.theme('Purple')
        layout = [
            [sg.Text("Concessionária ", justification='center', size=(20,1), font='Courier 15', background_color='pink', relief='sunken')],
            [sg.Button(button_text="Gerenciamento", font='Courier 12', size=(23,3))],
            [sg.Button(button_text="Venda", font='Courier 12', size=(23,3))],
            [sg.Button(button_text="Relatorio", font='Courier 12', size=(23,3))],
            [sg.Button(button_text="Sair", font='Courier 12', size=(23,3))]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button = window.read()[0]
        window.close()
        return button


    def tela_gerenciamento(self):
        layout = [
            [sg.Text("Gerenciamento", justification='center',size=(20,1), font='Courier 15', background_color='pink')],
            [sg.Button(button_text="Vendedores", font='Courier 12', size=(24,3))],
            [sg.Button(button_text="Clientes", font='Courier 12', size=(24,3))],
            [sg.Button(button_text="Carros", font='Courier 12', size=(24,3))],
            [sg.Button(button_text="Voltar", font='Courier 12', size=(24,3))]
        ]
        window = sg.Window("Título", no_titlebar=True, grab_anywhere=True).Layout(layout)
        
        button = window.read()[0]
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