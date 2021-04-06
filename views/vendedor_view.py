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
        os.system('cls' if os.name == 'nt' else 'clear')
        return opcao

    def cadastra(self):
        print("-----Cadastramento de Vendedor-----")
        nome = input("Nome do Vendedor:")
        telefone = input("Telefone do Vendedor:")
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
        print("\nLISTA DE VENDEDORES:")
        for vendedor in lista:
            print("#" + str(i))
            print("Nome: " + vendedor.nome)
            print("Telefone: "+ vendedor.telefone)
            print("ID: "+ str(vendedor.num_id))
            print("-----------------------------------")
            i += 1

    def vendedor_id(self):
        try:
            num_id = int(input("Digite o ID do vendedor a ser atualizado:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return 0
        else:
            return num_id

    def atualiza(self):
        print("\n-------Atualização de Vendedor--------")
        nome = input("Nome do Vendedor:")
        telefone = input("Telefone do Vendedor:")
        os.system('cls' if os.name == 'nt' else 'clear')
        return [nome, telefone]

    def remove(self):
        print("-----Remoção de Vendedor-----")
        try:
            num_id = int(input("Digite o ID do vendedor:"))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return 0
        else:
            return num_id

    def sucesso(self):
        print("Operação realizada com sucesso")
    
    def erro(self, mensagem_erro: str):
        print("\n" + mensagem_erro)
