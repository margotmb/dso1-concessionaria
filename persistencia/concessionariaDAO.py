from models.abstractDAO import AbstractDAO
from models.concessionaria import Concessionaria


class ConcessionariaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('concessionaria.pkl')

    def add(self, concessionaria: Concessionaria):
        if (concessionaria is not None) and isinstance(concessionaria, Concessionaria):
            super().add(0, concessionaria)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
