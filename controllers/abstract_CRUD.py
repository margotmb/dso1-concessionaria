from abc import ABC, abstractmethod


class AbstractCRUD(ABC):
    @abstractmethod
    def __init__(self, model, view):
        self.__model = model
        self.__view = view
    
    def run(self):
        opcao = self.__view.tela_principal()
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