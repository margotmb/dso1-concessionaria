import os


class CarroView():
    def __init__(self):
        pass

    def tela_principal(self):
        print("\n---- Gerenciamento de Carros ----")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Sair")
        print("-----------------------------------")
        opcao = input("Opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        return opcao

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
        print("\nLISTA DE carroS:")
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