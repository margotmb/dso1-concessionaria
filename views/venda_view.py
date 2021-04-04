from datetime import date as Date
import os


class VendaView():
    def __init__(self):
        pass

    def tela_de_vendas(self):
        try: 
            vendedor = int(input("ID do Vendedor: "))
            cliente = int(input("ID do Cliente: "))
            carro = int(input("ID do Carro: "))
            tempo_garantia = int(input("Tempo de Garantia em Anos: "))
        except ValueError as e:
            print('\nERRO: Caracter inválido: {}'.format(e))
            return
        else:
            data = Date.today()
            os.system('cls' if os.name == 'nt' else 'clear')
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
        try:
            vendedor_mais_carros = vendas[0].vendedor
            vendedor_maior_receita = vendas[0].vendedor
        except IndexError:
            print('\nERRO: Não há vendas cadastradas no sistema.')
        else:
            for venda in vendas:
                if venda.vendedor.carros_vendidos > vendedor_mais_carros.carros_vendidos:
                    vendedor_mais_carros = venda.vendedor
                if venda.vendedor.receita_gerada > vendedor_maior_receita.receita_gerada:
                    vendedor_maior_receita = venda.vendedor
            
            print("\nVendedor que mais vendeu carros: ")
            print("Nome: "+ vendedor_mais_carros.nome)
            print("Carros Vendidos: "+ str(vendedor_mais_carros.carros_vendidos))

            print("\nVendedor que mais gerou receita: ")
            print("Nome: " + vendedor_maior_receita)
            print("Receita Gerada: " + str(vendedor_maior_receita.receita_gerada))

    def venda_bem_sucedida(self):
        print("Venda bem sucedida")
