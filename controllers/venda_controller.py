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
        vendedor = None
        cliente = None
        carro = None

        for vend in self.__concessionaria.vendedores:
                if vend.num_id == info[0]:
                    vendedor = vend
                    print("ID Vendedor:" + str(vend.num_id))
        for cli in self.__concessionaria.clientes:
                if cli.num_id == info[1]:
                    cliente = cli
                    print("ID Cliente:" + str(cli.num_id))
        for car in self.__concessionaria.carros:
                if car.num_id == info[2]:
                    carro = car
                    print ("ID Carro:" + str(carro.num_id))

        #Se os 3 objetos existem no sistema, realiza a venda
        if vendedor is not None and cliente is not None and carro is not None:
            vendedor.carros_vendidos += 1
            vendedor.receita_gerada = vendedor.receita_gerada + carro.valor
            garantia = info[3]
            data = info[4]
            self.__concessionaria.nova_venda(Venda(vendedor, cliente, carro, garantia, data))
            self.__view.venda_bem_sucedida()

    def relatorio(self):
        self.__view.relatorio(self.__concessionaria.vendas)
