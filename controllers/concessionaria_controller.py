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

    def run(self):
        opcao = "X"
        while opcao != "0":
            opcao = self.__concessionaria_view.tela_principal()
            #Gerenciamento
            if opcao == "1":
                opcao = self.__concessionaria_view.tela_gerenciamento()

                #Escolhendo Controlador - Gerenciamento
                if opcao == "1":
                    vendedor_controller = VendedorController(self.__concessionaria_model)
                    vendedor_controller.run()
                elif opcao == "2":
                    self.__cliente_controller = ClienteController(self.__concessionaria_model)
                    self.__cliente_controller.run()
                elif opcao == "3":
                    self.__carro_controller = CarroController(self.__concessionaria_model)
                    self.__carro_controller.run()

            #Vendas
            if opcao == "2":
                venda_controller = VendaController(self.__concessionaria_model)
                venda_controller.nova_venda()