from models.concessionaria import Concessionaria
from models.venda import Venda
from views.venda_view import VendaView


class VendaController():
    def __init__(self, concessionaria: Concessionaria):
        self.__concessionaria = concessionaria
        self.__view = VendaView()

    def nova_venda(self):
        info = self.__view.tela_de_vendas()
        #info[0] -> ID_Vendedor
        #info[1] -> ID_Cliente
        #info[2] -> ID_Carro
        #info[3] -> Garantia
        #info[4] -> Data
        vendedor_existe = False
        cliente_existe = False
        carro_existe = False

        for vendedor in self.__concessionaria.vendedores:
                if vendedor.num_id == info[0]:
                    vendedor_existe = True
        for cliente in self.__concessionaria.vendedores:
                if cliente.num_id == info[1]:
                    cliente_existe = True
        for carro in self.__concessionaria.vendedores:
                if carro.num_id == info[2]:
                    carro_existe = True

        if vendedor_existe and cliente_existe and carro_existe:
            self.__concessionaria.nova_venda(Venda(info[0], info[1], info[2], info[3], info[4]))
    
    def relatorio(self):
        self.__view.relatorio(self.__concessionaria.vendas)
