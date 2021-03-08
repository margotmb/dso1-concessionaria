from pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str):
        super().__init__(nome, cpf, telefone)
