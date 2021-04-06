import os

class VendedorView():
    def __init__(self):
        pass

    def tela_principal(self):
        print("\n---- Gerenciamento de vendedor ----")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Sair")
        print("-----------------------------------")
        opcao = input("Opção: ")
        return opcao

    def cadastra(self):
        nome = input("Nome do Vendedor:")
        telefone = input("Telefone do Vendedor:")
        try:
            num_id = int(input("Numero de Identificação:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            return [nome, telefone, num_id]

    
    def lista(self, lista):
        os.system('cls' if os.name == 'nt' else 'clear')
        i = 0
        print("\nLISTA DE VENDEDORES:")
        for vendedor in lista:
            print("#" + str(i))
            print("Nome: " + vendedor.nome)
            print("Telefone: "+ vendedor.telefone)
            print("ID: "+ str(vendedor.num_id))
            print("-----------------------------------")
            i += 1

    def atualiza(self):
        print("\n-----------------------------------")
        nome = input("Nome do Vendedor:")
        telefone = input("Telefone do Vendedor:")
        try:
            num_id = int(input("Numero de Identificação:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
        else: 
            return [nome, telefone, num_id]

    def remove(self):
        try:
            num_id = int(input("ID do vendedor:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return 0
        else:    
            return num_id

    def sucesso(self):
        print("Operação realizada com sucesso")
    
    def erro(self):
        print("\nERRO")