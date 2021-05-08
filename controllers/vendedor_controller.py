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
                "Cadastrar" : self.cadastra,
                "Listar" : self.lista,
                "Atualizar" : self.atualiza,
                "Remover" : self.remove
        }
        opcao = self.__view.tela_principal()
        while opcao != "Voltar":
            func = op_dict[opcao]
            func()
            opcao = self.__view.tela_principal()

    def cadastra(self):
        dados = self.__view.cadastra()
        vendedores = list(self.__vendedorDAO.get_all())
        if dados is not None:
            for vendedor in vendedores:

                if vendedor.num_id == dados[0]:
                    self.__view.erro("Vendedor já existe")
                    return

                if vendedor.telefone == dados[2]:
                    #criar exceção
                    self.__view.erro("Telefone já existe no sistema")
                    return
                    
            #Nome, Telefone, ID
            vendedor = Vendedor(dados[1], dados[2], dados[0])
            self.__vendedorDAO.add(vendedor)
            self.__view.sucesso()

    def lista(self):
        vendedores = list(self.__vendedorDAO.get_all())
        self.__view.lista(vendedores)

    def atualiza(self):
        vendedores = list(self.__vendedorDAO.get_all())
        num_id = self.__view.vendedor_id(vendedores)

        if num_id != None:
            for vend in vendedores:
                if vend.num_id == num_id:
                    dados = self.__view.atualiza(vend.nome, vend.telefone, vend.num_id)
                    if dados is not None:
                        vend.nome = dados[0]
                        vend.telefone = dados[1]
                        self.__vendedorDAO.add(vend)
                        self.__view.sucesso()
                        return
                    else:
                        #Caso aperte voltar ou X
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