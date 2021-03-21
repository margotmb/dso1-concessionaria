from models.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome: str, telefone: str):
        super().__init__(nome, telefone)
