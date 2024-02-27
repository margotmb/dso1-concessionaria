class Carro:

    def __init__(self, marca: str, modelo: str, ano: int, valor: float, num_id: int):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__valor = valor
        self.__num_id = num_id

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: int):
        self.__valor = valor

    @property
    def num_id(self):
        return self.__num_id