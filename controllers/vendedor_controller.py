from models.vendedor import Vendedor
from views.vendedor_view import VendedorView
from persistencia.vendedorDAO import VendedorDAO


class VendedorController():
    def __init__(self):
        self.__vendedorDAO = VendedorDAO()
        self.__view = VendedorView()

    #Tela Principal de Vendedor
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
        info = self.__view.cadastra()
        vendedores = list(self.__vendedorDAO.get_all())
        if info is not None:
            for vendedor in vendedores:

                if vendedor.num_id == info[2]:
                    self.__view.erro("Vendedor já existe")
                    return

                if vendedor.telefone == info[1]:
                    #criar exceção
                    self.__view.erro("Telefone já existe no sistema")
                    return

            vendedor = Vendedor(info[1], info[2], info[0])
            print(type(info[2]))
            self.__vendedorDAO.add(vendedor)
            self.__view.sucesso()

    def lista(self):
        vendedores = list(self.__vendedorDAO.get_all())
        self.__view.lista(vendedores)

    def atualiza(self):
        vendedores = list(self.__vendedorDAO.get_all())
        identificacao = self.__view.vendedor_id(vendedores)
        
        for vend in vendedores:
            if vend.num_id == identificacao:
                info = self.__view.atualiza(vend.nome, vend.telefone)

                if info is not None:
                    vend.nome = info[0]
                    vend.telefone = info[1]
                    self.__view.sucesso()
                    return

        self.__view.erro("Vendedor não encontrado")

    def remove(self):
        vendedores = list(self.__vendedorDAO.get_all())
        num_id = self.__view.remove(vendedores)

        if num_id is not None:
            for vendedor in vendedores:
                if vendedor.num_id == num_id:
                    self.__vendedorDAO.remove(vendedor.num_id)
                    self.__view.sucesso()
                    return

            self.__view.erro("Vendedor não encontrado")
            self.remove()

    def lista_vendedores(self):
        return list(self.__vendedorDAO.get_all())