'''
exercicio de Herança e Polimorfismo

Exercício 7: 

crie uma classe Retangulo com os atributos:
largura, altura

a classe Retangulo deve ter o método:
area - calcula a área do retângulo (largura * altura)

crie uma classe Quadrado que herda de Retangulo e, ao ser instanciada, deve:
passar um único valor para largura e altura
sobrescrever o método area() para o cálculo da área do quadrado
'''

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        area_final = self.largura * self.altura
        print(area_final)

class Quadrado(Retangulo):
    def __init__(self, lado):   # aq a gnt só inicializa um atributo (lado)
        super().__init__(lado, lado)    # aq define o mesmo valor de largura e altura

    # não preciso refazer a def area porque vou utilizar ela da mesma forma, ja q estou atribuindo "2 valores" com o super()

retangulo = Retangulo(10, 20)
quadrado = Quadrado(10)

retangulo.area()
quadrado.area()
