from models.pessoa import Pessoa


class Vendedor(Pessoa):

    def __init__(self, nome: str, telefone: str):
        super().__init__(nome, telefone)
