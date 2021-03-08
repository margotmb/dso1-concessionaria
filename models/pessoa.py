from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, cpf: str, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
