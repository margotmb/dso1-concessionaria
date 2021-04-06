import os


class ClienteView():
    def __init__(self):
        pass

    def tela_principal(self):
        print("\n---- Gerenciamento de clientes ----")
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

