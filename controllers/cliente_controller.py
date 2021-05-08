from persistencia.clienteDAO import ClienteDAO
from models.cliente import Cliente
from views.cliente_view import ClienteView


class ClienteController():
    def __init__(self):
        self.__clienteDAO = ClienteDAO()
        self.__view = ClienteView()

    #Tela Principal de Cliente
    def run(self):
        op_dict = {
                "1" : self.cadastra,
                "2" : self.lista,
                "3" : self.atualiza,
                "4" : self.remove
        }
        opcao = self.__view.tela_principal()
        while opcao != "0":
            func = op_dict[opcao]
            func()
            opcao = self.__view.tela_principal()

    def cadastra(self):
        lista = list(self.__clienteDAO.get_all())
        dados = self.__view.cadastra()

        if dados is not None:
            for cliente in lista:
                
                #Verifica ID
                if cliente.num_id == dados[0]:
                    self.__view.erro("Cliente já existe")
                    return
                #Verifica Telefone
                if cliente.telefone == dados[2]:
                    self.__view.erro("Telefone já existe no sistema")
                    return

            #Nome, Telefone, ID
            cliente = Cliente(dados[1], dados[2], dados[0])
            self.__clienteDAO.add(cliente)
            self.__view.sucesso()

    def lista(self):
        clientes = list(self.__clienteDAO.get_all())
        self.__view.lista(clientes)

    def atualiza(self):
        clientes = list(self.__clienteDAO.get_all())
        num_id = self.__view.cliente_id(clientes)

        if num_id != None:
            for cliente in clientes:
                if cliente.num_id == num_id:
                    dados = self.__view.atualiza(cliente.nome, cliente.telefone, cliente.num_id)
                    if dados is not None:
                        cliente.nome = dados[0]
                        cliente.telefone = dados[1]
                        self.__clienteDAO.add(cliente)
                        self.__view.sucesso()
                        return
                    else:
                        #Caso aperte voltar ou X
                        return
            self.__view.erro("Cliente não encontrado")

    def remove(self):
        clientes = list(self.__clienteDAO.get_all())
        num_id = self.__view.remove(clientes)
        if num_id is not None:
            for cliente in clientes:
                if cliente.num_id == num_id:
                    self.__clienteDAO.remove(cliente.num_id)
                    self.__view.sucesso()
                    return
            self.__view.erro("Cliente não encontrado")
    
    def lista_clientes(self):
        return list(self.__clienteDAO.get_all())