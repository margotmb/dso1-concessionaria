from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
  
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
