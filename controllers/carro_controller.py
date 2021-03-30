from views.carro_view import CarroView


class CarroController():
    def __init__(self, model):
        self.__concessionaria_model = model
        self.__carro_view = CarroView()

    def run(self):
        pass