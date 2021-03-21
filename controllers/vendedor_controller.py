from models.concessionaria import Concessionaria
from models.vendedor import Vendedor
from views.vendedor_view import VendedorView
from controllers.abstract_CRUD import AbstractCRUD


class VendedorController(AbstractCRUD):
    def __init__(self, model: Concessionaria, view = VendedorView):
        super().__init__(model, view)

    def adiciona(self):
        pass

    def lista(self):
        pass

    def atualiza(self):
        pass

    def remove(self):
        pass
