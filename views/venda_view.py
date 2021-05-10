from datetime import date as Date
import PySimpleGUI as sg
from views.abstract_view_CRUD import AbstractViewCRUD
from models.vendedor import Vendedor
from models.cliente import Cliente
from models.carro import Carro


class VendaView(AbstractViewCRUD):
    def __init__(self):
        pass

    def tela_de_vendas(self, vendedores, clientes, carros):
        #Seleciona um vendedor
        lista_vendedores = self.gera_lista_dados(vendedores)
        if lista_vendedores != None:
            vendedor_id = super().tela_input_id(lista_vendedores, "Escolha um Vendedor")
            if vendedor_id != None:
                for vend in vendedores:
                    if vend.num_id == vendedor_id:
                        vendedor = vend
            else:
                return None
        else:
            self.erro("ERRO: Não há vendedores cadastrados")
            return

        #Seleciona um cliente
        lista_clientes = self.gera_lista_dados(clientes)
        if lista_clientes != None:
            cliente_id = super().tela_input_id(lista_clientes, "Escolha um Cliente")
            if cliente_id != None:
                for client in clientes:
                    if client.num_id == cliente_id:
                        cliente = client
            else:
                return None
        else:
            self.erro("ERRO: Não há vendedores cadastrados")
            return
        
        #Seleciona um carro
        lista_carros = self.gera_lista_dados(carros)
        if lista_carros != None:
            carro_id = super().tela_input_id(lista_carros, "Escolha um Carro")
            if carro_id != None:
                for car in carros:
                    if car.num_id == carro_id:
                        carro = car
            else:
                return None
        else:
            self.erro("ERRO: Não há vendedores cadastrados")
            return
        #Seleciona garantia em anos
        layout = [
            [sg.Text("Tempo de garantia em anos:", size=(25, 1)), sg.InputText()],
            [sg.Button("Submit"), sg.Button("Voltar")]
        ]

        window = sg.Window("Garantia").Layout(layout)

        button, values = window.read()

        #Seta Data
        data = Date.today()
        window.close()
        if button == "Submit":
            tempo_garantia = values[0]
            try:
                tempo_garantia = int(tempo_garantia)
            except ValueError:
                self.erro("ERRO: Dado Inválido")
            else:
                return [vendedor, cliente, carro, tempo_garantia, data]
        else:
            return None

    def relatorio(self, vendas: list, counter: int):
        layout = [
                [sg.Output(size=(40,30), key="_output_")],
                [sg.Button('Listar'), sg.Button('Voltar')],
        ]  
        window = sg.Window('RELATÓRIO - VENDAS').Layout(layout)
        button = window.Read(timeout=5)
        num = 0
        #Loop da Janela
        while button[0] != 'Voltar':
            lista = []
            for venda in vendas:
                num = "#" + str(num)
                vendedor = "Vendedor: " + venda.vendedor.nome
                cliente = "Cliente: "+ venda.cliente.nome
                carro = "Carro: "+ venda.carro.modelo +" - "+ str(venda.carro.ano)
                valor = "Valor: R$" + str(venda.carro.valor)
                lista.extend([num, vendedor, cliente, carro, valor, "\n"])
            try:
                vendedor_mais_carros = vendas[0].vendedor
                vendedor_maior_receita = vendas[0].vendedor
            except IndexError:
                sg.popup('\nERRO: Não há vendas cadastradas no sistema.')
                window.close()
                return
            else:
                for venda in vendas:
                    if venda.vendedor.carros_vendidos > vendedor_mais_carros.carros_vendidos:
                        vendedor_mais_carros = venda.vendedor
                    if venda.vendedor.receita_gerada > vendedor_maior_receita.receita_gerada:
                        vendedor_maior_receita = venda.vendedor

                lista.append("\n#Vendedor que mais vendeu carros: ")
                lista.append("Nome: "+ vendedor_mais_carros.nome)
                lista.append("Carros Vendidos: "+ str(vendedor_mais_carros.carros_vendidos))

                lista.append("\n#Vendedor que mais gerou receita: ")
                lista.append("Nome: " + vendedor_maior_receita.nome)
                lista.append("Receita Gerada: R$" + str(vendedor_maior_receita.receita_gerada))

                window.FindElement('_output_').Update('')
                for j in lista:
                    print(j)

                button = window.Read()
        window.close()

    def venda_bem_sucedida(self):
        sg.popup("Venda bem sucedida")

    def gera_lista_dados(self, objetos):
        lista = []
        
        try:
            if isinstance(objetos[0], Vendedor):
                for item in objetos:                
                    num_id = "ID: " + str(item.num_id)
                    nome = "Nome: " + item.nome
                    telefone = "Telefone: " + item.telefone
                    carros_vendidos = "Carros Vendidos: " + str(item.carros_vendidos)
                    receita_gerada = "Receita Gerada: R$" + str(item.receita_gerada)
                    lista.extend([num_id,nome,telefone,carros_vendidos,receita_gerada, "\n"])
        except IndexError:
            return None

        
        try:
            if isinstance(objetos[0], Cliente):
                for item in objetos:
                    num_id = "ID: " + str(item.num_id)
                    nome = "Nome: " + item.nome
                    telefone = "Telefone: " + item.telefone
                    lista.extend([num_id,nome,telefone, "\n"])
        except IndexError:
            return None

        
        try:
            if isinstance(objetos[0], Carro):
                for item in objetos:
                    num_id = "ID: " + str(item.num_id)
                    marca = "Marca: " + item.marca
                    modelo = "Modelo: " + item.modelo
                    ano = "Ano: " + str(item.ano)
                    valor = "Valor: R$" + str(item.valor)
                    lista.extend([num_id, marca, modelo, ano, valor, "\n"])
        except IndexError:
            return None

        
        return lista
