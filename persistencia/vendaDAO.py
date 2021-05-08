from persistencia.abstractDAO import AbstractDAO
from models.venda import Venda
import PySimpleGUI as sg

class VendaDAO(AbstractDAO):
    def __init__(self):
        super().__init__('vendas.pkl')
    
    def add(self, venda: Venda, counter: int):
        sg.popup("ENTROU NO DAO")
        if isinstance(counter, int) and (venda is not None) and isinstance(venda, Venda):
            sg.popup("ENTROU NO IF")
            super().add(counter, venda)
            sg.popup("ADICIONOU NO DAO")
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)
