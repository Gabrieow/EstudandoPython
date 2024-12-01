'''
exercício 3:

exercício utilizando herança

criar uma classe Pessoa com os atributos:
nome, idade, sexo
Com o metodo fazer_aniversario() que aumenta a idade da pessoa em 1

criar uma classe Aluno que herda de pessoa e adiciona os atributos:
matricula, curso
co o metodo apresentar() que imprime uma mensagem dizendo o nome do aluno e o curso que está matriculado
'''

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Feliz aniversário, {self.nome}!\nVocê fez {self.idade} anos!")

class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, matricula, curso):
        super().__init__(nome, idade, sexo)     # super serve pra colocar a herança em pratica, se nao usar super eu nao consigo usar as defs criadas na classe pai
        self.matricula = matricula
        self.curso = curso

    def apresentar(self):
        print(f"Nome: {self.nome}\nCurso matriculado: {self.curso}")

pai = Pessoa("Jair", 52, "Masculino")

pai.fazer_aniversario()

eu = Aluno("Gabriel", 20, "Masculino", 12345, "ADS")

eu.fazer_aniversario()
eu.apresentar()

# eu consigo fazer aniversario e me apresentar porque sou Pessoa e Aluno
# pai nao consegue porque ele só é Pessoa, não é Aluno
# exercício simples de herança