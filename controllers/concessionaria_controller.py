from models.concessionaria import Concessionaria
from views.concessionaria_view import ConcessionariaView


class ConcessionariaController:

    def __init__(self):
        self.__model = Concessionaria()
        self.__view =  ConcessionariaView()

    def run(self):
        pass
