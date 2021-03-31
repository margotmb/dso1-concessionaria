import os


class ConcessionariaView:

    def __init__(self):
        pass

    def tela_principal(self):
        print("-----------------------------------")
        print("Gerenciamento de Concessionária")
        print("1 - Gerenciamento")
        print("2 - Venda")
        print("3 - Relatório")
        print("-----------------------------------")
        opcao = input("Opção: ")
        return opcao

    def tela_gerenciamento(self):
        print("-----------------------------------")
        print("1 - Vendedores")
        print("2 - Clientes")
        print("3 - Carros")
        print("-----------------------------------")
        opcao = input("Opção: ")
        os.system('cls')
        return opcao
