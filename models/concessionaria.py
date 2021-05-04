from models.carro import Carro
from models.cliente import Cliente
from models.vendedor import Vendedor
from models.venda import Venda
from models.carroDAO import CarroDAO
from models.clienteDAO import ClienteDAO
from models.vendedorDAO import VendedorDAO
from models.vendaDAO import VendaDAO


class Concessionaria:
    def __init__(self):
        self.__carro_DAO = CarroDAO()
        # self.__carros = [Carro("Chevrolet", "Sedan", 2019, 50000, 1),
        #                  Carro("Chevrolet", "Hatch", 2018, 40000, 2),
        #                  Carro("Ford", "Hatch", 2020, 45000, 3),
        #                  Carro("Hyundai", "Hatch", 2020, 45000, 4),
        #                  Carro("Toyota", "Sedan", 2019, 60000, 5),
        #                  Carro("Ford", "Pickup", 2021, 80000, 6)]
        self.__cliente_DAO = ClienteDAO()
        # self.__clientes = [Cliente("Márcio", "988144896", 101),
        #                    Cliente("João", "991168765", 102),
        #                    Cliente("Aline", "988148696", 103),
        #                    Cliente("Ana", "975148571", 104),
        #                    Cliente("Antônio", "991405869", 105)]
        self.__vendedor_DAO = VendedorDAO()
        #self.__vendedores = [Vendedor("Vendedor A", "991540932", 201), Vendedor("Vendedor B", "988128231", 202)]
        self.__venda_DAO = VendaDAO()

    @property
    def carros(self):
        return list(self.__carro_DAO.get_all())

    @property
    def clientes(self):
        return list(self.__cliente_DAO.get_all())

    @property
    def vendedores(self):
        return list(self.__vendedor_DAO.get_all())

    @property
    def vendas(self):
        return list(self.__venda_DAO.get_all())

    def cadastra_objeto(self, objeto):
        if isinstance(objeto, Carro):
            self.__carro_DAO.add(objeto)
        if isinstance(objeto, Cliente):
            self.__cliente_DAO.add(objeto)
        if isinstance(objeto, Vendedor):
            self.__vendedor_DAO.add(objeto)

    def remove_objeto(self, objeto):
        if isinstance(objeto, Carro):
            self.__carro_DAO.remove(objeto.num_id)
        if isinstance(objeto, Cliente):
            self.__cliente_DAO.remove(objeto.num_id)
        if isinstance(objeto, Vendedor):
            self.__vendedor_DAO.remove(objeto.num_id)

    def nova_venda(self, venda: Venda, counter):
        self.__venda_DAO.add(venda, counter)
