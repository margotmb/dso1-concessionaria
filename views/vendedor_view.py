class VendedorView():
    def __init__(self):
        pass

    def tela_principal(self):
        print("Gerenciamento de vendedor")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Sair")
        opcao = input()
        return opcao

    def cadastra(self):
        nome = input("Nome do Vendedor:")
        telefone = input("Telefone do Vendedor:")
        num_id = input("Numero de Identificação:")
        return [nome, telefone, num_id]
    
    def lista(self, lista):
        print(lista)

    def atualiza(self):
        nome = input("Nome do Vendedor:")
        telefone = input("Telefone do Vendedor:")
        num_id = input("Numero de Identificação:")
        return [nome, telefone, num_id]

    def remove(self):
        num_id = input("ID do vendedor:")
        return num_id