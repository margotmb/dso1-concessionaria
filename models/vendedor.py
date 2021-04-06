from models.pessoa import Pessoa


class Vendedor(Pessoa):

    def __init__(self, nome: str, telefone: str, num_id: int):
        super().__init__(nome, telefone)
        self.__num_id = num_id
        self.__carros_vendidos = 0
        self.__receita_gerada = 0.0

    @property
    def num_id(self):
        return self.__num_id

    @num_id.setter
    def num_id(self, num_id: int):
         self.__num_id = num_id

    @property
    def carros_vendidos(self):
        return self.__carros_vendidos

    @carros_vendidos.setter
    def carros_vendidos(self, carros_vendidos: int):
        self.__carros_vendidos = carros_vendidos

    @property
    def receita_gerada(self):
        return self.__receita_gerada

    @receita_gerada.setter
    def receita_gerada(self, receita_gerada: float):
        self.__receita_gerada = receita_gerada