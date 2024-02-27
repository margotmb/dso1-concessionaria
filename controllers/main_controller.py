from models.concessionaria import Concessionaria
from views.main_view import MainView
from controllers.cliente_controller import ClienteController
from controllers.vendedor_controller import VendedorController
from controllers.carro_controller import CarroController
from controllers.venda_controller import VendaController


class MainController:

    def __init__(self):
        self.__concessionaria_view =  MainView()
        self.__vendedor_controller = VendedorController()
        self.__cliente_controller = ClienteController()
        self.__carro_controller = CarroController()

    def run(self):
        op_dict_main = {
                "Gerenciamento" : self.gerenciamento,
                "Venda" : self.nova_venda,
                "Relatorio" : self.relatorio,
                "Sair" : self.sair
        }
        op_main = self.__concessionaria_view.tela_principal()

        while op_main!= "Sair":
            func = op_dict_main[op_main]
            func()
            op_main = self.__concessionaria_view.tela_principal()
    
    def gerenciamento(self):
        op_dict = {
            "Vendedores": self.__vendedor_controller.run,
            "Clientes": self.__cliente_controller.run,
            "Carros": self.__carro_controller.run
        }

        op_manage = self.__concessionaria_view.tela_gerenciamento()
        try:
            func = op_dict[op_manage]
            func()
        except KeyError:
            return
    
    def nova_venda(self):
        venda_controller = VendaController(self.__vendedor_controller.lista_vendedores(), self.__cliente_controller.lista_clientes(), self.__carro_controller.lista_carros())
        venda_controller.nova_venda()

    def relatorio(self):
        venda_controller = VendaController(self.__vendedor_controller.lista_vendedores(), self.__cliente_controller.lista_clientes(), self.__carro_controller.lista_carros())
        venda_controller.relatorio()
    def sair(self):
        exit()

    # def edit_concessionaria(self):
    #     new_info = self.__concessionaria_view.tela_edicao(self.__concessionaria_model.nome, self.__concessionaria_model.endereco, self.__concessionaria_model.cnpj)
    #     self.__concessionaria_model.nome = new_info[0]
    #     self.__concessionaria_model.endereco = new_info[1]
    #     self.__concessionaria_model.cnpj = new_info[2]
    #     self.__concessionaria_DAO.add(self.__concessionaria_model)        