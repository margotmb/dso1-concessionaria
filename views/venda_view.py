from datetime import date as Date

class VendaView():
    def __init__(self):
        pass

    def tela_de_vendas(self):
        vendedor = int(input("ID do Vendedor: "))
        cliente = int(input("ID do Cliente: "))
        carro = int(input("ID do Carro: "))
        tempo_garantia = int(input("Tempo de Garantia: "))
        data = Date.today()
        return [vendedor, cliente, carro, tempo_garantia, data]