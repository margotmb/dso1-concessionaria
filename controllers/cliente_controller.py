from models.concessionaria import Concessionaria
from models.cliente import Cliente
from views.cliente_view import ClienteView

class ClienteController():
    def __init__(self, model: Concessionaria):
        self.__concessionaria_model = model
        self.__cliente_view = ClienteView()

    def run(self):
        opcao = self.__cliente_view.tela_principal()
        if opcao == "1":
            self.adiciona()
        elif opcao == "2":
            self.lista()
        elif opcao == "3":
            self.atualiza()
        elif opcao == "4":
            self.remove()

    def adiciona(self):
        pass

    def lista(self):
        pass

    def atualiza(self):
        pass

    def remove(self):
        pass