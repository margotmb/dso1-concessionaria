from datetime import date as Date
import os


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
    
    def relatorio(self, vendas: list):
        i = 0
        print("\nLISTA DE VENDAS:")
        for venda in vendas:
            print("#" + str(i))
            print("Vendedor: " + venda.vendedor.nome)
            print("Cliente: "+ venda.cliente.nome)
            print("Carro: "+ venda.carro.modelo +" - "+ str(venda.carro.ano))
            print("-----------------------------------")
            i += 1