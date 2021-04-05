from models.concessionaria import Concessionaria
from models.vendedor import Vendedor
from views.vendedor_view import VendedorView


class VendedorController():
    def __init__(self, concessionaria: Concessionaria):
        self.__concessionaria = concessionaria
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

        if info is not None:
            for vendedor in self.__concessionaria.vendedores:
                if vendedor.num_id == info[2]:
                    self.__view.erro("Vendedor já existe")
                    return

            vendedor = Vendedor(info[0], info[1], info[2])
            self.__concessionaria.cadastra_objeto(vendedor)
            self.__view.sucesso()

    def lista(self):
        self.__view.lista(self.__concessionaria.vendedores)

    def atualiza(self):
        self.lista()
        identificacao = self.__view.vendedor_id()
        for vend in self.__concessionaria.vendedores:
            if vend.num_id == identificacao:
                info = self.__view.atualiza()
                if info is not None:
                    vend.nome = info[0]
                    vend.telefone = info[1]
                    return
        self.__view.erro("Vendedor não encontrado")

    def remove(self):
        self.lista()
        num_id = self.__view.remove()
        for vendedor in self.__concessionaria.vendedores:
            if vendedor.num_id == num_id:
                self.__concessionaria.remove_objeto(vendedor)
                self.__view.sucesso()
                return
        self.__view.erro("Vendedor não encontrado")
