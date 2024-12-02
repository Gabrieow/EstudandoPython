'''
Exercício 10: Sistema de Reservas de Hotéis

Crie uma classe Reserva com os atributos:
cliente, data_entrada, data_saida, valor_total

A classe Reserva deve ter o método:
calcular_valor(): calcula o valor total da reserva (dependendo do número de diárias, por exemplo).
'''

class Reserva:
    def __init__(self, cliente, data_entrada, data_saida, valor_total):
        self.cliente = cliente
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.valor_total = valor_total
    
    def calcular_valor():
        

cliente1 = Reserva("Gabriel", "01/12/2024", "02/12/2024", 100)


