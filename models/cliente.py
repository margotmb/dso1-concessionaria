from models.pessoa import Pessoa


class Cliente(Pessoa):

    def __init__(self, nome: str, telefone: str, num_id: int):
        super().__init__(nome, telefone)
        self.__num_id = num_id
    
    @property
    def num_id(self):
        return self.__num_id