nome = input("Digite o seu nome: ")
while len(nome) <= 3:
    nome = input("Digite o seu nome [MAIOR QUE 3 CARACTERES]: ")

idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Digite a sua idade [ENTRE 0 E 150]: "))

salario = float(input("Digite o seu salário: "))
while salario <= 0:
    salario = float(input("Digite o seu salário [MAIOR QUE 0]: "))

sexo = input("Digite o seu sexo [f, m]: ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Digite o seu sexo [f OU m]: ")

estado_civil = input("Digite o seu estado civil [s, c, v, d]: ")
while estado_civil not in ('s', 'c', 'v', 'd'):
    estado_civil = input("Digite o seu estado civil [s, c, v, d]: ")

print("Critérios correspondidos, cadastro efetuado.")