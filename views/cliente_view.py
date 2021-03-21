class ClienteView():
    def __init__(self):
        pass

    def tela_principal(self):
        print("Gerenciamento de clientes")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Sair")
        opcao = input()
        return opcao