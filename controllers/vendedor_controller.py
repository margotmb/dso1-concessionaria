from models.concessionaria import Concessionaria
from models.vendedor import Vendedor
from views.vendedor_view import VendedorView
from controllers.abstract_CRUD import AbstractCRUD


class VendedorController(AbstractCRUD):
    def __init__(self, concessionaria: Concessionaria, view = VendedorView):
        super().__init__(concessionaria, view)

    #def run() -in-> AbstractCRUD

    def adiciona(self):
        info = self.__view.adiciona()

        duplicado = False
        for vendedor in self.__concessionaria.vendedores:
            if vendedor.num_id == info[2]:
                duplicado = True
        
        if not duplicado:
            vendedor = Vendedor(info[0], info[1], info[2])
            self.__concessionaria.cadastra_objeto(vendedor)

    def lista(self):
        self.__view.lista(self.__concessionaria.vendedores)

    def atualiza(self):
        info = self.__view.atualiza()
        for vendedor in self.__concessionaria.vendedores:
            if vendedor.num_id == info[2]:
                vendedor.nome = info[0]
                vendedor.telefone = info[1]

    def remove(self):
        num_id = self.__view.remove()
        for vendedor in self.__concessionaria.vendedores:
            if vendedor.num_id == num_id:
                self.__concessionaria.remove_objeto(vendedor)
        
