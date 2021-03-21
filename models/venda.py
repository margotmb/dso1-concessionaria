from models.vendedor import Vendedor
from models.cliente import Cliente
from models.carro import Carro
from datetime import date as Date


class Venda:

    def __init__(self, vendedor: Vendedor, cliente: Cliente, carro: Carro, garantia: int, data: Date):
        self.__vendedor = vendedor
        self.__cliente = cliente
        self.__carro = carro
        self.__tempo_garantia = 0
        self.__data = data

