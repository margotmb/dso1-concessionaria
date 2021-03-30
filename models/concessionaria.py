from models.carro import Carro
from models.cliente import Cliente
from models.vendedor import Vendedor


class Concessionaria:

    def __init__(self):
        self.__carros = []
        self.__clientes = []
        self.__vendedores = [Vendedor("NOME", "1231231", 50)]
        self.__vendas = []
    
    @property
    def carros(self):
        return self.__carros
    
    @property
    def clientes(self):
        return self.__clientes

    @property
    def vendedores(self):
        return self.__vendedores

    def cadastra_objeto(self, objeto):
        if isinstance(objeto, Carro):
            self.__carros.append(objeto)
        if isinstance(objeto, Cliente):
            self.__clientes.append(objeto)
        if isinstance(objeto, Vendedor):
            self.__vendedores.append(objeto)

    def remove_objeto(self, objeto):
        if isinstance(objeto, Carro):
            self.__carros.remove(objeto)
        if isinstance(objeto, Cliente):
            self.__clientes.remove(objeto)
        if isinstance(objeto, Vendedor):
            self.__vendedores.remove(objeto)
