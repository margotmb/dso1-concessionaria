from models.concessionaria import Concessionaria
from views.concessionaria_view import ConcessionariaView
from controllers.cliente_controller import ClienteController
from controllers.vendedor_controller import VendedorController
from controllers.carro_controller import CarroController
from controllers.venda_controller import VendaController
import os


class ConcessionariaController:

    def __init__(self):
        self.__concessionaria_model = Concessionaria()
        self.__concessionaria_view =  ConcessionariaView()
        self.__vendedor_controller = VendedorController(self.__concessionaria_model)
        self.__cliente_controller = ClienteController(self.__concessionaria_model)
        self.__carro_controller = CarroController(self.__concessionaria_model)
        self.__venda_controller = VendaController(self.__concessionaria_model)

    def run(self):
        op_main = "X"
        while op_main != "0":
            op_main = self.__concessionaria_view.tela_principal()
            #Gerenciamento
            if op_main == "1":
                op_manage = self.__concessionaria_view.tela_gerenciamento()

                #Escolhendo Controlador - Gerenciamento
                if op_manage == "1":
                    self.__vendedor_controller.run()
                elif op_manage == "2":
                    self.__cliente_controller.run()
                elif op_manage == "3":
                    self.__carro_controller.run()
            #Vendas
            elif op_main == "2":
                self.__venda_controller.nova_venda()
            #Relatório
            elif op_main == "3":
                self.__venda_controller.relatorio()
            