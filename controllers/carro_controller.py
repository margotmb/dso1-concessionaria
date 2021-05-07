from models.carro import Carro
from views.carro_view import CarroView
from models.carroDAO import CarroDAO

class CarroController():
    def __init__(self):
        self.__carroDAO = CarroDAO()
        self.__carro_view = CarroView()

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
        lista = list(self.__carroDAO.get_all())
        info = self.__carro_view.cadastra()
        if info is not None:
            for carro in lista:
                if carro.num_id == info[4]:
                    self.__carro_view.erro("Carro já existe")
                    return
            carro = Carro(info[0], info[1], info[2], info[3], info[4])
            self.__carroDAO.add(carro)
            self.__carro_view.sucesso()

    def lista(self):
        self.__carro_view.lista(list(self.__carroDAO.get_all()))

    def atualiza(self):
        lista = list(self.__carroDAO.get_all())
        identificacao = self.__carro_view.carro_id()
        for carro in lista:
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
        lista = list(self.__carroDAO.get_all())
        num_id = self.__carro_view.remove()
        for carro in lista:
            if carro.num_id == num_id:
                self.__carroDAO.remove(carro.num_id)
                self.__carro_view.sucesso()
                return
        self.__carro_view.erro("Carro não encontrado")
    
    def lista_carros(self):
        return list(self.__carroDAO.get_all())