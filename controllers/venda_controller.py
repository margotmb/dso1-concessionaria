from persistencia.vendaDAO import VendaDAO
from models.venda import Venda
from views.venda_view import VendaView


class VendaController():
    def __init__(self, lista_vendedores, lista_clientes, lista_carros):
        self.__vendedores = lista_vendedores
        self.__clientes = lista_clientes
        self.__carros = lista_carros
        self.__vendaDAO = VendaDAO()
        self.__view = VendaView()
        self.__counter = 0

    def nova_venda(self):
        info = self.__view.tela_de_vendas()
        #info[0] -> ID_Vendedor
        #info[1] -> ID_Cliente
        #info[2] -> ID_Carro
        #info[3] -> Garantia
        #info[4] -> Data
        vendedor = None
        cliente = None
        carro = None

        for vend in self.__vendedores:
                if vend.num_id == info[0]:
                    vendedor = vend
                    #print("ID Vendedor:" + str(vend.num_id))
        for cli in self.__clientes:
                if cli.num_id == info[1]:
                    cliente = cli
                    #print("ID Cliente:" + str(cli.num_id))
        for car in self.__carros:
                if car.num_id == info[2]:
                    carro = car
                    #print ("ID Carro:" + str(carro.num_id))

        #Se os 3 objetos existem no sistema, realiza a venda
        if vendedor is not None and cliente is not None and carro is not None:
            vendedor.carros_vendidos += 1
            vendedor.receita_gerada = vendedor.receita_gerada + carro.valor
            garantia = info[3]
            data = info[4]
            self.__counter += 1
            self.__vendaDAO.add(Venda(vendedor, cliente, carro, garantia, data), self.__counter)
            self.__view.venda_bem_sucedida()

    def relatorio(self):
        self.__view.relatorio(list(self.__vendaDAO.get_all()))
