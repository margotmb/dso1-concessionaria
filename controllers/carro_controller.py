from models.carro import Carro
from views.carro_view import CarroView
from models.concessionaria import Concessionaria


class CarroController():
    def __init__(self, concessionaria: Concessionaria):
        self.__concessionaria = concessionaria
        self.__carro_view = CarroView()

   #Tela Principal de Carros
    def run(self):
        op_dict = {
                "1" : self.cadastra,
                "2" : self.lista,
                "3" : self.atualiza,
                "4" : self.remove
        }
        opcao = self.__carro_view.tela_principal()
        while opcao != "0":
            func = op_dict[opcao]
            func()
            opcao = self.__carro_view.tela_principal()

    def cadastra(self):
        info = self.__carro_view.cadastra()
        if info is not None:
            for carro in self.__concessionaria.carros:
                ###
                if carro.num_id == info[4]:
                    self.__carro_view.erro("Carro já existe")
                    return
            carro = Carro(info[0], info[1], info[2], info[3], info[4])
            self.__concessionaria.cadastra_objeto(carro)
            self.__carro_view.sucesso()

    def lista(self):
        self.__carro_view.lista(self.__concessionaria.carros)

    def atualiza(self):
        self.lista()
        identificacao = self.__carro_view.carro_id()
        for carro in self.__concessionaria.carros:
            if carro.num_id == identificacao:
                info = self.__carro_view.atualiza()
                if info is not None:
                    carro.marca = info[0]
                    carro.modelo = info[1]
                    carro.ano = info[2]
                    carro.valor = info[3]
                    self.__carro_view.sucesso()
                    return
        self.__carro_view.erro("Carro não encontrado")

    def remove(self):
        self.lista()
        num_id = self.__carro_view.remove()
        for carro in self.__concessionaria.carros:
            if carro.num_id == num_id:
                self.__concessionaria.remove_objeto(carro)
                self.__carro_view.sucesso()
                return
        self.__carro_view.erro("Carro não encontrado")