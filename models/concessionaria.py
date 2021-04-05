from models.carro import Carro
from models.cliente import Cliente
from models.vendedor import Vendedor
from models.venda import Venda


class Concessionaria:

    def __init__(self):
        self.__carros = [Carro("Chevrolet", "Sedan", 2019, 50000, 1),
                         Carro("Chevrolet", "Hatch", 2018, 40000, 2),
                         Carro("Ford", "Hatch", 2020, 45000, 3),
                         Carro("Hyundai", "Hatch", 2020, 45000, 4),
                         Carro("Toyota", "Sedan", 2019, 60000, 5),
                         Carro("Ford", "Pickup", 2021, 80000, 6)]
        self.__clientes = [Cliente("Márcio", "988144896", 101),
                           Cliente("João", "991168765", 102),
                           Cliente("Aline", "988148696", 103),
                           Cliente("Ana", "975148571", 104),
                           Cliente("Antônio", "991405869", 105)]
        self.__vendedores = [Vendedor("Vendedor 1", "991540932", 201), Vendedor("Vendedor 2", "988128231", 202)]
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
