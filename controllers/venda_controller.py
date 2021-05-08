from persistencia.vendaDAO import VendaDAO
from models.venda import Venda
from views.venda_view import VendaView
import PySimpleGUI as sg


class VendaController():
    def __init__(self, lista_vendedores, lista_clientes, lista_carros):
        self.__vendedores = lista_vendedores
        self.__clientes = lista_clientes
        self.__carros = lista_carros
        self.__vendaDAO = VendaDAO()
        self.__view = VendaView()
        self.__counter = 0

    def nova_venda(self):
        dados = self.__view.tela_de_vendas(self.__vendedores, self.__clientes, self.__carros)
        #dados[0] -> ID_Vendedor
        #dados[1] -> ID_Cliente
        #dados[2] -> ID_Carro
        #dados[3] -> Garantia
        #dados[4] -> Data
        if dados is not None:
            vendedor = dados[0]
            cliente = dados[1]
            carro = dados[2]
        else:
            return
    
        vendedor.carros_vendidos += 1
        try:
            vendedor.receita_gerada = vendedor.receita_gerada + carro.valor
            garantia = dados[3]
            data = dados[4]
        except Exception as e:
            sg.popup("ERRO: {}".format(e))
        
        self.__counter += 1
        self.__vendaDAO.add(Venda(vendedor, cliente, carro, garantia, data), self.__counter)
        self.__view.venda_bem_sucedida()

    def relatorio(self):
        vendas = list(self.__vendaDAO.get_all())
        self.__view.relatorio(vendas, self.__counter)
