with open('dados_pessoas.txt', 'r') as file:
    linhas = file.readlines()

dados = [linha.strip().split(',') for linha in linhas]

cabecalho = dados[0]
linhas_dados = dados[1:]

############

# Exercício 1:

print("Exercício 1: Crie um programa que leia o arquivo de dados e exiba-os no formato: [nome], [idade], [cidade], [salario].\n\n")
for linha in linhas_dados:
    print(f"Nome: {linha[0]}\nIdade: {linha[1]}\nCidade: {linha[3]}\nSalário: {linha[4]}")

###########

# Exercício 2:

print("Exercício 2: Crie um programa que leia o arquivo e exiba apenas as pessoas com idade maior que 30 anos. Exiba o nome e a cidade dessas pessoas.\n\n")
for linha in linhas_dados:
    if linha[1] > 30:
        print(f"Nome: {linha[0]}\nCidade: {linha[2]}")

############

# Exercício 3:

print("Exercício 3: Crie um programa que leia o arquivo e calcule a soma total de todos os salários. No final, exiba o valor total.\n\n")
salarios = int(linha[3] for linha in linhas_dados)
valor_total = sum(salarios)
print(f"Valor total: {salarios}")

############

# Exercício 4:

print("Exercício 4: Crie um programa que leia o arquivo e conte quantas pessoas moram em cada idade. Exiba o nome da cidade e a quantidade de pessoas que moram nela.\n\n")

contagem_cidades = {} 

for linha in linhas_dados:
    cidade = linha[2]
    if cidade in contagem_cidades:  #2. quando o código já tiver rodado, o dicionário vai começar a ter cidades + contador de quantas vezes ela apareceu, então se aparecer dnv, o if adiciona +1 no contador.
        contagem_cidades[cidade] += 1
    else:   # 1. o código "começa" aqui. Como o dicionário está vazio, ele vai começar adicionando as cidades a partir do else
        contagem_cidades[cidade] = 1

for cidade, quantidade in contagem_cidades.items():
    print(f"{cidade}: {quantidade} pessoas")

###########

# Exercício 5:

print("Exercício 5: Crie um programa que pergunte o nome de uma pessoa e aumente seu salário em 5%. Salve o arquivo atualizado.\n\n")

nome_user = input("Digite o nome de uma pessoa para aumentar o salário: ")

for linha in linhas_dados:
    if linha[0].lower() == nome_user.lower():   # ignora a forma que o usuario escreve (maiusculas e minusculas)
        linha[3] = str(float(linha[3]) * 1.05)

with open('dados_pessoas.txt', 'w') as file: # Salva e atualiza o arquivo
    file.write(','.join(cabecalho) + '\n')
    for linha in linhas_dados:
        file.write(','.join(linha) + '\n')

print(f"Salário de {nome_user} atualizado com sucesso!")

############

print("Exercício 6: Crie um programa que pergunte o nome de uma pessoa e, se ela existir no arquivo, remova-a. Salve o arquivo atualizado.\n\n")

nome_user = input("Digite o nome da pessoa para remover: ")

linhas_atualizadas = [cabecalho]

for linha in linhas_dados:
    if linha[0].lower() != nome_user.lower(): # caso o nome da linha seja diferente do nome inserido pelo usuario
        linhas_atualizadas.append(linha)    # o programa insere o nome dentro da lista linhas_atualizadas, se for igual, ele ignora e nao adiciona (removendo da lista)

with open('dados_pessoas.txt', 'w') as file:
    for linha in linhas_atualizadas:
        file.write(','.join(linha) + '\n')

print(f"{nome_user} foi removido do arquivo com sucesso!") 