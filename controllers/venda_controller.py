from models.concessionaria import Concessionaria
from models.venda import Venda
from views.venda_view import VendaView


class VendaController():
    def __init__(self, concessionaria: Concessionaria):
        self.__concessionaria = concessionaria
        self.__view = VendaView()

    def run(self):
        info = self.__view.tela_de_vendas()
        #info[0] -> ID_Vendedor
        #info[1] -> ID_Cliente
        #info[2] -> ID_Carro
        #info[3] -> Garantia
        #info[4] -> Data