"""
exercicio de Polimorfismo

Exercício 6:

crie uma classe Funcionario com os atributos:
nome, salario

a classe Funcionario deve ter o método:
aumentar_salario(valor): aumenta o salário do funcionário.

crie uma classe Gerente que herda de Funcionario e tenha um atributo adicional:
bonus: valor adicional que o gerente recebe.

a classe Gerente deve sobrescrever o método aumentar_salario() para incluir o bônus.
"""

class Funcionario:  # criando classe funcionario
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentar_salario(self, valor):
        self.salario += valor   # atualizando salario com valor inserido pelo usuario
        print(f"O salário teve um aumento em R${valor}.")

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)     # herdando da classe funcionario
        self.bonus = 1.50   # adicionando novo atributo bonus de 1.5
    
    def aumentar_salario(self, valor):
        aumento = valor * self.bonus
        self.salario += aumento
        print(f"O salário teve um aumento em R${aumento}.")
    
funcionario1 = Funcionario("João", 1500.00)
Gerente1 = Gerente("Gabriel", 3000.00)

Gerente1.aumentar_salario(200)
funcionario1.aumentar_salario(200)

# no fim ficou parecendo mais um exercício de herança, mas o polimorfismo está presente de forma indireta onde eu atualizo uma função preexistente de outra classe
