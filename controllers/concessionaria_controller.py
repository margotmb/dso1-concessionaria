from models.concessionaria import Concessionaria
from views.concessionaria_view import ConcessionariaView
from controllers.cliente_controller import ClienteController
from controllers.vendedor_controller import VendedorController


class ConcessionariaController:

    def __init__(self):
        self.__concessionaria_model = Concessionaria()
        self.__concessionaria_view =  ConcessionariaView()

    def run(self):
        pass