'''
exercício de Composição

Exercício 9: 

crie uma classe Endereco com os atributos:
logradouro, numero, bairro, cidade

crie uma classe Pessoa que tenha um atributo:
endereco (uma instância da classe Endereco).

a classe Pessoa deve ter o método:
mostrar_endereco(): exibe o endereço da pessoa.
'''

class Endereco:
    def __init__(self, logradouro, numero, bairro, cidade):
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mostrar_endereco(self):
        print(f"Endereço de {self.nome}: {self.endereco.logradouro}, {self.endereco.numero}, {self.endereco.bairro}, {self.endereco.cidade}")

meu_endereco = Endereco("João Amaro", 68, "Pinheirinho", "Curitiba") # nao, nao eh meu endereço de verdade

pessoa = Pessoa("Carlos", meu_endereco)

pessoa.mostrar_endereco

