from models.concessionaria import Concessionaria
from views.concessionaria_view import ConcessionariaView
from controllers.cliente_controller import ClienteController
from controllers.vendedor_controller import VendedorController
from controllers.carro_controller import CarroController
from controllers.venda_controller import VendaController
from models.concessionariaDAO import ConcessionariaDAO


class ConcessionariaController:

    def __init__(self):
        self.__concessionaria_DAO = ConcessionariaDAO()
        self.__concessionaria_model = self.__concessionaria_DAO.get(0)

        if self.__concessionaria_model is None:
            self.__concessionaria_model = Concessionaria()
            self.__concessionaria_DAO.add(self.__concessionaria_model)

        self.__concessionaria_view =  ConcessionariaView()
        self.__vendedor_controller = VendedorController(self.__concessionaria_model)
        self.__cliente_controller = ClienteController(self.__concessionaria_model)
        self.__carro_controller = CarroController(self.__concessionaria_model)
        self.__venda_controller = VendaController(self.__concessionaria_model)

    def run(self):
        op_dict_main = {
                "1" : self.gerenciamento,
                "2" : self.__venda_controller.nova_venda,
                "3" : self.__venda_controller.relatorio,
                "4" : self.edit_concessionaria
        }
        op_main = self.__concessionaria_view.tela_principal(self.__concessionaria_model.nome, self.__concessionaria_model.endereco, self.__concessionaria_model.cnpj)

        while op_main!= "0":
            func = op_dict_main[op_main]
            func()
            op_main = self.__concessionaria_view.tela_principal(self.__concessionaria_model.nome, self.__concessionaria_model.endereco, self.__concessionaria_model.cnpj)

    def gerenciamento(self):
        op_dict = {
            "1": self.__vendedor_controller.run,
            "2": self.__cliente_controller.run,
            "3": self.__carro_controller.run
        }

        op_manage = self.__concessionaria_view.tela_gerenciamento()
        try:
            func = op_dict[op_manage]
            func()
        except KeyError:
            return
        

    def edit_concessionaria(self):
        new_info = self.__concessionaria_view.tela_edicao(self.__concessionaria_model.nome, self.__concessionaria_model.endereco, self.__concessionaria_model.cnpj)
        self.__concessionaria_model.nome = new_info[0]
        self.__concessionaria_model.endereco = new_info[1]
        self.__concessionaria_model.cnpj = new_info[2]
        self.__concessionaria_DAO.add(self.__concessionaria_model)        