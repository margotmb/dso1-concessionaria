from models.concessionaria import Concessionaria
from views.venda_view import VendaView


class VendaController():
    def __init__(self, concessionaria: Concessionaria):
        self.__concessionaria = concessionaria
        self.__view = VendaView()

    def run(self):
        pass