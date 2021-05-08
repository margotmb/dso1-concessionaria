from models.abstractDAO import AbstractDAO
from models.venda import Venda


class VendaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('vendas.pkl')
    
    def add(self, venda: Venda, counter: int):
        if isinstance(counter, int) and (venda is not None) and isinstance(venda, venda):
            super().add(counter, venda)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
