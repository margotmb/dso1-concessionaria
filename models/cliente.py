from models.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome: str, telefone: str, saldo: float, cpf: str):
        super().__init__(nome, telefone)
        self.__saldo = saldo
        self.__cpf = cpf
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def cpf(self):
        return self.__cpf
