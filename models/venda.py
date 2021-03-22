from models.vendedor import Vendedor
from models.cliente import Cliente
from models.carro import Carro
from datetime import date as Date


class Venda:

    def __init__(self, vendedor: Vendedor, cliente: Cliente, carro: Carro, tempo_garantia: int, data: Date):
        self.__vendedor = vendedor
        self.__cliente = cliente
        self.__carro = carro
        self.__tempo_garantia = 0
        self.__data = data

    @property
    def vendedor(self):
        return self.__vendedor

    @property
    def cliente(self):
        return self.__cliente

    @property
    def carro(self):
        return self.__carro

    @property
    def tempo_garantia(self):
        return self.__tempo_garantia

    @property
    def data(self):
        return self.__data     
