from models.abstractDAO import AbstractDAO
from models.cliente import Cliente


class ClienteDAO(AbstractDAO):
    def __init__(self):
        super().__init__('clientes.pkl')
    
    def add(self, cliente: Cliente):
        if isinstance(cliente.num_id, int) and (cliente is not None) and isinstance(cliente, Cliente):
            super().add(cliente.num_id, cliente)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)