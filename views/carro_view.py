import os
import PySimpleGUI as sg


class CarroView():
    def __init__(self):
        pass

    def tela_principal(self):
        layout = [
            [sg.Text("----Carros----", justification='center',size=(20,1))],
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
        print("-----Cadastramento de Carro-----")
        marca = input("Marca do carro:")
        modelo = input("Modelo do carro:")
        try:
            ano = int(input("Ano do Carro: "))
            valor = float(input("Valor do Carro em Reais: "))
            num_id = int(input("Numero de Identificação:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return None
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return [marca, modelo, ano, valor, num_id]

    def lista(self, lista):
        os.system('cls' if os.name == 'nt' else 'clear')
        i = 0
        print("\nLISTA DE CARROS:")
        for carro in lista:
            print("#" + str(i))
            print("Marca: " + carro.marca)
            print("Modelo: "+ carro.modelo)
            print("Ano: " + str(carro.ano))
            print("Valor: R$" + str(carro.valor))
            print("ID: "+ str(carro.num_id))
            print("-----------------------------------")
            i += 1

    def carro_id(self):
        try:
            num_id = int(input("Digite o ID do carro a ser atualizado:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return 0
        else:
            return num_id

    def atualiza(self):
        print("\n-------Atualização de carro--------")
        marca = input("Marca do carro:")
        modelo = input("Modelo do carro:")
        try:
            ano = int(input("Ano do Carro: "))
            valor = float(input("Valor do Carro em Reais: "))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return None
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return [marca, modelo, ano, valor]

    def remove(self):
        print("-----Remoção de carro-----")
        try:
            num_id = int(input("Digite o ID do carro:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return 0
        else:
            return num_id

    def sucesso(self):
        print("Operação realizada com sucesso")
    
    def erro(self, mensagem_erro: str):
        print("\n" + mensagem_erro)
