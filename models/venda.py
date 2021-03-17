from vendedor import Vendedor
from cliente import Cliente
from carro import Carro


class Venda:

    def __init__(self, vendedor: Vendedor, cliente: Cliente, carro: Carro):
        self.__vendedor = vendedor
        self.__cliente = cliente
        self.__carro = carro
