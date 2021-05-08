from models.carro import Carro
from views.carro_view import CarroView
from persistencia.carroDAO import CarroDAO

class CarroController():
    def __init__(self):
        self.__carroDAO = CarroDAO()
        self.__view = CarroView()

    def run(self):
        op_dict = {
                "1" : self.cadastra,
                "2" : self.lista,
                "3" : self.atualiza,
                "4" : self.remove
        }
        opcao = self.__view.tela_principal()
        while opcao != "0":
            func = op_dict[opcao]
            func()
            opcao = self.__view.tela_principal()

    def cadastra(self):
        dados = self.__view.cadastra()
        vendedores = list(self.__carroDAO.get_all())
        if dados is not None:
            for vendedor in vendedores:

                if vendedor.num_id == dados[0]:
                    self.__view.erro("Carro já existe")
                    return
                    
            #Marca, Modelo, Ano, Valor, ID
            carro = Carro(dados[1], dados[2], dados[3], dados[4], dados[0])
            self.__carroDAO.add(carro)
            self.__view.sucesso()

    def lista(self):
        carros = list(self.__carroDAO.get_all())
        self.__view.lista(carros)

    def atualiza(self):
        encontrado = False
        carros = list(self.__carroDAO.get_all())
        num_id = self.__view.carro_id(carros)

        if num_id != None:
            for car in carros:
                if car.num_id == num_id:
                    #Se encontrou -> Chama View de Atualizar
                    dados = self.__view.atualiza(car.marca, car.modelo, car.ano, car.valor, car.num_id)
                    if dados is not None:
                        car.marca = dados[0]
                        car.modelo = dados[1]
                        car.ano = dados[2]
                        car.valor = dados[3]
                        self.__carroDAO.add(car)
                        self.__view.sucesso()
                        encontrado == True
                    else:
                        #Caso aperte voltar ou X
                        return
            if not encontrado:
                self.__view.erro("Vendedor não encontrado")

    def remove(self):
        carros = list(self.__carroDAO.get_all())
        num_id = self.__view.remove(carros)

        if num_id is not None:
            for carro in carros:
                if carro.num_id == num_id:
                    self.__carroDAO.remove(carro.num_id)
                    self.__view.sucesso()
                    return

            self.__view.erro("Carro não encontrado")
            self.remove()
    
    def lista_carros(self):
        return list(self.__carroDAO.get_all())