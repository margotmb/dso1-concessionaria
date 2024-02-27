from persistencia.abstractDAO import AbstractDAO
from models.carro import Carro


class CarroDAO(AbstractDAO):
    def __init__(self):
        super().__init__('carros.pkl')
    
    def add(self, carro: Carro):
        if isinstance(carro.num_id, int) and (carro is not None) and isinstance(carro, Carro):
            super().add(carro.num_id, carro)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)