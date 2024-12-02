'''
Exercício 10: Sistema de Reservas de Hotéis

Crie uma classe Reserva com os atributos:
cliente, data_entrada, data_saida, valor_total

A classe Reserva deve ter o método:
calcular_valor(): calcula o valor total da reserva (dependendo do número de diárias, por exemplo).
'''

from datetime import datetime

class Reserva:
    def __init__(self, cliente, data_entrada, data_saida, valor_diaria):
        self.cliente = cliente
        self.data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y")
        self.data_saida = datetime.strptime(data_saida, "%d/%m/%Y")
        self.valor_diaria = valor_diaria
        self.valor_total = 0
    
    def calcular_valor(self):
        dias = (self.data_saida - self.data_entrada).days
        if dias > 0:
            self.valor_total = dias * self.valor_diaria
        else:
            raise ValueError("A data de saída não pode ser antes da data de entrada.")
        return self.valor_total

reserva1 = Reserva("Gabriel Henrique", "09/12/2024", "16/12/2024", 200)
valor = reserva1.cacular_valor()
print(f"Reserva de {reserva.cliente}:\nValor Total: R${valor:.2f}")
