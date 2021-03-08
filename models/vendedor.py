from pessoa import Pessoa


class Vendedor(Pessoa):

    def __init__(self, nome: str, cpf: str, telefone: str):
        super().__init__(nome, cpf, telefone)
