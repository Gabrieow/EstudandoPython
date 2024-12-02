'''
exercício de Agregação

Exercício 8:

crie uma classe Departamento com os atributos:
nome, funcionarios (lista de funcionários do departamento)

a classe Departamento deve ter o método:
adicionar_funcionario(funcionario) - adiciona um funcionário ao departamento.

crie uma classe Funcionario com os atributos:
nome, cargo

crie uma classe Empresa com os atributos:
nome_empresa, departamentos (lista de departamentos)

a classe Empresa deve ter o método:
adicionar_departamento(departamento) - adiciona um departamento à empresa.
'''
class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)


class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
class Empresa:
    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.departamentos = []
    
    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)

funcionario1 = Funcionario("João", "Analista")
funcionario2 = Funcionario("Maria", "Desenvolvedora")

departamento_ti = Departamento("TI")
departamento_ti.adicionar_funcionario(funcionario1)
departamento_ti.adicionar_funcionario(funcionario2)

empresa = Empresa("TechCorp")
empresa.adicionar_departamento(departamento_ti)

for departamento in empresa.departamentos:
    print(f"Departamento: {departamento.nome}")
    for funcionario in departamento.funcionarios:
        print(f"Funcionário: {funcionario.nome}, Cargo: {funcionario.cargo}")

# seguiu bastante a lógica dos últimos exercícios, basicamente criamos 3 classes q possuem agregação entre sí
# inicializamos listas para os departamentos e funcionarios
# e dps adicionamos o conteúdo da lista com append
# por fim fazemos a consulta com laço de repetição