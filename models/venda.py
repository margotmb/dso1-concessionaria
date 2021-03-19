from models.vendedor import Vendedor
from models.cliente import Cliente
from models.carro import Carro


class Venda:

    def __init__(self, vendedor: Vendedor, cliente: Cliente, carro: Carro):
        self.__vendedor = vendedor
        self.__cliente = cliente
        self.__carro = carro
