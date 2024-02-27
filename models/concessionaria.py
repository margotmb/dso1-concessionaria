from models.carro import Carro
from models.cliente import Cliente
from models.vendedor import Vendedor
from models.venda import Venda


class Concessionaria:
    def __init__(self):
        self.__nome = '<nome>'
        self.__endereco = '<endereco>'
        self.__cnpj = '<cnpj>'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
