''' 
Exercício 1: 

Criar uma clase carro com os atributos: 
Modelo, ano, cor, velocidade_maxima;

Com os metodos: 
Acelerar() - aumenta a velocidade em 10und.
Frear() - diminui a velocidade em 10 unidades, sem permitir que a velocidade fique abaixo de 0.
mostrar_info() - exibe as informações do carro, como modelo, ano, cor e velocidade máxima.

'''

class Carro:    # Construindo a classe
    def __init__ (self, modelo, ano, cor, velocidade_maxima):   # Colocando os atributos
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.velocidade = 0     # Atributo para a variável velocidade q vou usar mais tarde
    
    def acelerar(self, multiplicador):  # adicionei um multiplicador aqui pra não precisar ficar digitando o metodo acelerar toda hora
        print("Acelerando!")
        self.velocidade += 10 * multiplicador   # adiciono 10und * multiplicador
        if self.velocidade >= self.velocidade_maxima:   # se a multiplicaçao for passar a velocidade maxima
            self.velocidade = self.velocidade_maxima    # a gente define a velocidade pra velocidade maxima
            print("Velocidade máxima atingida!")    # e dps exibe um aviso falando q ela foi atingida
        else:
            print(f"Velocidade atual: {self.velocidade}")   # aq a gnt so exibe a velocidade msm

    def frear(self):
        print("Freiando!")
        if self.velocidade <= 0:    # se a velocidade for menor ou igual a 0
            self.velocidade = 0     # a gnt define ela pra 0 e emite um aviso  falando q nao eh possivel frear
            print("Não é possível frear!")
        else:
            self.velocidade -= 10   # se for maior q 0 a gente freia e printa a velocidade atual
            print(f"{self.velocidade}km/h")
    
    def mostrar_info(self):     # aq eh so um print das informaçoes inseridas
        print(f"Modelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}\nVelocidade Máxima: {self.velocidade_maxima}")


# é legal salientar que esse código só funciona pq o acelerar e frear sempre são de 10und cada, entao nunca vai ter numero quebrado pra dar problema no codigo

meu_carro = Carro("Lancer GT", 2015, "Preto", 198)


meu_carro.acelerar(1)
meu_carro.frear()
meu_carro.frear()

