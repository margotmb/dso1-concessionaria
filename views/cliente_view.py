import os
import PySimpleGUI as sg


class ClienteView():
    def __init__(self):
        pass

    def tela_principal(self):
        layout = [
            [sg.Text("----Clientes----", justification='center',size=(20,1))],
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
        print("-----Cadastramento de Cliente-----")
        nome = input("Nome do Cliente:")
        telefone = input("Telefone do Cliente:")
        try:
            num_id = int(input("Numero de Identificação:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return None
        else:
            if telefone.isdecimal():
                os.system('cls' if os.name == 'nt' else 'clear')
                return [nome, telefone, num_id]
            else:
                print("Telefone Inválido")

    def lista(self, lista):
        os.system('cls' if os.name == 'nt' else 'clear')
        i = 0
        print("\nLISTA DE CLIENTES:")
        for cliente in lista:
            print("#" + str(i))
            print("Nome: " + cliente.nome)
            print("Telefone: "+ cliente.telefone)
            print("ID: "+ str(cliente.num_id))
            print("-----------------------------------")
            i += 1

    def cliente_id(self):
        try:
            num_id = int(input("Digite o ID do cliente a ser atualizado:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return 0
        else:
            return num_id

    def atualiza(self):
        print("\n-------Atualização de Cliente--------")
        nome = input("Nome do Cliente:")
        telefone = input("Telefone do Cliente:")
        os.system('cls' if os.name == 'nt' else 'clear')
        return [nome, telefone]

    def remove(self):
        print("-----Remoção de Cliente-----")
        try:
            num_id = int(input("Digite o ID do cliente:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return 0
        else:
            return num_id

    def sucesso(self):
        print("Operação realizada com sucesso")
    
    def erro(self, mensagem_erro: str):
        print("\n" + mensagem_erro)

