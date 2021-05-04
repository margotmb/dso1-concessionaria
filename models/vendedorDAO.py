from models.abstractDAO import AbstractDAO
from models.vendedor import Vendedor


class VendedorDAO(AbstractDAO):
    def __init__(self):
        super().__init__('vendedores.pkl')
    
    def add(self, vendedor: Vendedor):
        if isinstance(vendedor.num_id, int) and (vendedor is not None) and isinstance(vendedor, Vendedor):
            super().add(vendedor.num_id, vendedor)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
