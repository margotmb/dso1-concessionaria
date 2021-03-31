from models.carro import Carro
from models.cliente import Cliente
from models.vendedor import Vendedor
from models.venda import Venda


class Concessionaria:

    def __init__(self):
        self.__carros = [Carro("Sedan", 2010, 50000, 10)]
        self.__clientes = [Cliente("José", "1231231231", 1000000, 20)]
        self.__vendedores = [Vendedor("Vendedor 1", "1231231", 50)]
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
    
    @property
    def vendas(self):
        return self.__vendas

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
    
    def nova_venda(self, venda: Venda):
        self.__vendas.append(venda)
