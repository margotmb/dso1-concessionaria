from models.concessionaria import Concessionaria
from models.vendedor import Vendedor
from views.vendedor_view import VendedorView


class VendedorController():
    def __init__(self, concessionaria: Concessionaria):
        self.__concessionaria = concessionaria
        self.__view = VendedorView()

    #Tela Principal de Vendedor
    def run(self):
        opcao = self.__view.tela_principal()
        while opcao != "0":
            if opcao == "1":
                self.cadastra()
            elif opcao == "2":
                self.lista()
            elif opcao == "3":
                self.atualiza()
            elif opcao == "4":
                self.remove()
            opcao = self.__view.tela_principal()

    def cadastra(self):
        info = self.__view.cadastra()

        if info is not None:
            for vendedor in self.__concessionaria.vendedores:
                if vendedor.num_id == info[2]:
                    self.__view.erro()
                    return

            vendedor = Vendedor(info[0], info[1], info[2])
            self.__concessionaria.cadastra_objeto(vendedor)
            self.__view.sucesso()

    def lista(self):
        self.__view.lista(self.__concessionaria.vendedores)

    def atualiza(self):
        self.lista()
        for vendedor in self.__concessionaria.vendedores:
            if vendedor.num_id == self.__view.vendedor_id():
                info = self.__view.atualiza()
                if info is not None:
                    vendedor.nome = info[0]
                    vendedor.telefone = info[1]

    def remove(self):
        self.lista()
        num_id = self.__view.remove()
        for vendedor in self.__concessionaria.vendedores:
            if vendedor.num_id == num_id:
                self.__concessionaria.remove_objeto(vendedor)
