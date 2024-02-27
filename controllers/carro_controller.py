from models.carro import Carro
from views.carro_view import CarroView
from persistencia.carroDAO import CarroDAO

class CarroController():
    def __init__(self):
        self.__carroDAO = CarroDAO()
        self.__view = CarroView()

    def run(self):
        op_dict = {
                "Cadastrar" : self.cadastra,
                "Listar" : self.lista,
                "Atualizar" : self.atualiza,
                "Remover" : self.remove
        }
        opcao = self.__view.tela_principal()
        while opcao != "Voltar":
            func = op_dict[opcao]
            func()
            opcao = self.__view.tela_principal()

    def cadastra(self):
        dados = self.__view.cadastra()
        carros = list(self.__carroDAO.get_all())

        if dados is not None:
            for carro in carros:
                if carro.num_id == dados[0]:
                    self.__view.erro("Carro já existe")
                    return

               
            #Marca, Modelo, Ano, Valor, ID
            try:
                dados[3] = int(dados[3])
                dados[4] = float(dados[4])
                dados[0] = int(dados[0])
            except ValueError:
                self.__view.erro("DADO INVÁLIDO")
            else:
                carro = Carro(dados[1], dados[2], dados[3], dados[4], dados[0])
                self.__carroDAO.add(carro)
                self.__view.sucesso()

    def lista(self):
        carros = list(self.__carroDAO.get_all())
        self.__view.lista(carros)

    def atualiza(self):
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
                        car.ano = int(dados[2])
                        car.valor = float(dados[3])
                        self.__carroDAO.add(car)
                        self.__view.sucesso()
                        return
                    else:
                        #Caso aperte voltar ou X
                        return
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
        lista = list(self.__carroDAO.get_all())
        return lista