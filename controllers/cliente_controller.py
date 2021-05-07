from models.clienteDAO import ClienteDAO
from models.cliente import Cliente
from views.cliente_view import ClienteView


class ClienteController():
    def __init__(self):
        self.__clienteDAO = ClienteDAO()
        self.__cliente_view = ClienteView()

    #Tela Principal de Cliente
    def run(self):
        op_dict = {
                "1" : self.cadastra,
                "2" : self.lista,
                "3" : self.atualiza,
                "4" : self.remove
        }
        opcao = self.__cliente_view.tela_principal()
        while opcao != "0":
            func = op_dict[opcao]
            func()
            opcao = self.__cliente_view.tela_principal()

    def cadastra(self):
        lista = list(self.__clienteDAO.get_all())
        info = self.__cliente_view.cadastra()
        if info is not None:
            for cliente in lista:
                if cliente.num_id == info[2]:
                    self.__cliente_view.erro("Cliente já existe")
                    return
                if cliente.telefone == info[1]:
                    self.__cliente_view.erro("Telefone já existe no sistema")
                    return
            cliente = Cliente(info[0], info[1], info[2])
            self.__clienteDAO.add(cliente)
            self.__cliente_view.sucesso()

    def lista(self):
        self.__cliente_view.lista(list(self.__clienteDAO.get_all()))

    def atualiza(self):
        lista = list(self.__clienteDAO.get_all())
        identificacao = self.__cliente_view.cliente_id()
        for cliente in lista:
            if cliente.num_id == identificacao:
                info = self.__cliente_view.atualiza()
                if info is not None:
                    cliente.nome = info[0]
                    cliente.telefone = info[1]
                    self.__cliente_view.sucesso()
                    return
        self.__cliente_view.erro("Cliente não encontrado")

    def remove(self):
        lista = list(self.__clienteDAO.get_all())
        num_id = self.__cliente_view.remove()
        for cliente in lista:
            if cliente.num_id == num_id:
                self.__clienteDAO.remove(cliente.num_id)
                self.__cliente_view.sucesso()
                return
        self.__cliente_view.erro("Cliente não encontrado")
    
    def lista_clientes(self):
        return list(self.__clienteDAO.get_all())