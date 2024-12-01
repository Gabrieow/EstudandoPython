# Abrindo o arquivo 'dados_pessoas.txt' para leitura e armazenando as linhas
with open('dados_pessoas.txt', 'r') as file:
    linhas = file.readlines()  # Lê todas as linhas do arquivo

# Separando os dados de cada linha em uma lista, considerando que os dados são separados por vírgula
dados = [linha.strip().split(',') for linha in linhas]

# Armazenando o cabeçalho (primeira linha) e os dados das pessoas (resto das linhas)
cabecalho = dados[0]
linhas_dados = dados[1:]

#####################

# Exercício 1: Filtrar pessoas com idade entre 25 e 40 anos e exibir nome e cidade
print("Exercício 1: Filtre as pessoas que têm idade entre 25 e 40 anos e Exiba o nome e a cidade dessas pessoas.\n")
for linha in linhas_dados:
    if 25 <= int(linha[1]) <= 40:  # Verifica se a idade está entre 25 e 40
        print(f"Nome: {linha[0]}, Cidade: {linha[2]}")  # Exibe nome e cidade

#####################

# Exercício 2: Solicitar ao usuário o nome de uma cidade e exibir a média salarial e pessoas com salário acima da média
print("Exercício 2: Crie um programa que solicite ao usuário o nome de uma cidade e então mostre a média salarial dos habitantes dessa cidade e exiba o nome e o salário das pessoas que têm salário acima da média dessa cidade.\n")
# Coleta de salários para calcular a média
salarios = [int(linha[3]) for linha in linhas_dados]
cidade_user = input("Digite o nome de uma das seguintes cidades: São Paulo, Rio de Janeiro, Belo Horizonte, Porto Alegre, Curitiba\n")

# Filtra as pessoas pela cidade informada
pessoas_da_cidade = [linha for linha in linhas_dados if linha[2] == cidade_user]
# Calcula a média salarial da cidade
salarios_cidade = [int(linha[3]) for linha in pessoas_da_cidade]
media_salarial = sum(salarios_cidade) / len(salarios_cidade) if salarios_cidade else 0

# Exibe a média salarial e as pessoas com salário acima da média
print(f"Média Salarial da cidade {cidade_user}: {media_salarial}")
for linha in pessoas_da_cidade:
    if int(linha[3]) > media_salarial:  # Verifica se o salário é acima da média
        print(f"Nome: {linha[0]}, Salário: {linha[3]}")

#####################

# Exercício 3: Ordenar pessoas pelo salário do menor para o maior
print("Exercício 3: Crie um programa que ordene as pessoas pelo salário, do menor para o maior e exiba as pessoas e seus respectivos salários de forma ordenada.\n")
# Ordena as pessoas pela coluna de salário (índice 3) do menor para o maior
dados_ordenados = sorted(linhas_dados, key=lambda x: int(x[3]))
# Exibe os dados ordenados
for linha in dados_ordenados:
    print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}, Salário: {linha[3]}")

######################

# Exercício 4: Identificar e exibir pessoas com nome duplicado
print("Exercício 4: Identifique e exiba as pessoas com nome duplicado no arquivo.\n")
# Cria um dicionário para contar as ocorrências de cada nome
nomes_contados = {}
for linha in linhas_dados:
    nome = linha[0]
    if nome not in nomes_contados:
        nomes_contados[nome] = []
    nomes_contados[nome].append(linha)

# Exibe as pessoas com nomes duplicados
for nome, pessoas in nomes_contados.items():
    if len(pessoas) > 1:  # Se o nome se repetir mais de uma vez
        print(f"Nome Duplicado: {nome}")
        for pessoa in pessoas:
            print(f"  Idade: {pessoa[1]}, Cidade: {pessoa[2]}, Salário: {pessoa[3]}")

######################

# Exercício 5: Aumentar o salário de uma pessoa em 10% e salvar o arquivo
print("Exercício 5: Crie um programa que pergunte o nome de uma pessoa e caso essa pessoa existir no arquivo, aumente seu salário em 10%. Salve o arquivo atualizado.\n")
nome_user = input("Digite o nome de uma pessoa: ")
# Itera pelas linhas para aumentar o salário de quem for o nome fornecido
for linha in linhas_dados:
    if nome_user == linha[0]:
        linha[3] = str(int(linha[3]) * 1.10)  # Aumenta o salário em 10%

# Salva o arquivo com os dados atualizados
with open('dados_pessoas.txt', 'w') as file:
    file.write(cabecalho + '\n')  # Escreve o cabeçalho
    for linha in linhas_dados:
        file.write(','.join(linha) + '\n')  # Escreve as linhas atualizadas

####################

# Exercício 6: Remover uma pessoa do arquivo e salvar as alterações
print("Exercício 6: Crie um programa que pergunte o nome de uma pessoa e se essa pessoa existir no arquivo, remova-a. Salve o arquivo atualizado.\n")
nome_user = input("Digite o nome de uma pessoa para remover: ")
# Filtra as linhas para remover a pessoa com o nome informado
linhas_dados = [linha for linha in linhas_dados if linha[0] != nome_user]

# Salva o arquivo com a pessoa removida
with open('dados_pessoas.txt', 'w') as file:
    file.write(cabecalho + '\n')  # Escreve o cabeçalho
    for linha in linhas_dados:
        file.write(','.join(linha) + '\n')  # Escreve as linhas restantes

#######################

# Exercício 7: Gerar relatório com quantidade de pessoas em cada faixa etária
print("Exercício 7: Crie um programa que gere um relatório com a quantidade de pessoas em cada faixa etária e exiba a quantidade de pessoas em sua faixa etária.\n")
# Dicionário para contar as faixas etárias
faixas = {
    "18-30": 0,
    "31-40": 0,
    "41-50": 0,
    "51-60": 0,
    "60+": 0
}

# Conta as pessoas em cada faixa etária
for linha in linhas_dados:
    idade = int(linha[1])
    if 18 <= idade <= 30:
        faixas["18-30"] += 1
    elif 31 <= idade <= 40:
        faixas["31-40"] += 1
    elif 41 <= idade <= 50:
        faixas["41-50"] += 1
    elif 51 <= idade <= 60:
        faixas["51-60"] += 1
    elif idade > 60:
        faixas["60+"] += 1

# Exibe o número de pessoas em cada faixa etária
for faixa, count in faixas.items():
    print(f"Faixa etária {faixa}: {count} pessoas")

##################

# Exercício 8: Calcular salário médio de uma faixa etária fornecida pelo usuário
print("Exercício 8: Crie um programa que pergunte ao usuário uma faixa etária, calcule e exiba o salário médio das pessoas dessa faixa etária.\n")
# Solicita os limites da faixa etária
faixa1_user = int(input("Digite o 1º valor da faixa etária: "))
faixa2_user = int(input("Digite o 2º valor da faixa etária: "))
# Filtra as pessoas dentro da faixa etária fornecida
pessoas_na_faixa = [linha for linha in linhas_dados if faixa1_user <= int(linha[1]) <= faixa2_user]
# Coleta os salários da faixa etária
salarios_na_faixa = [int(linha[3]) for linha in pessoas_na_faixa]
# Calcula a média salarial
media_salarial = sum(salarios_na_faixa) / len(salarios_na_faixa) if salarios_na_faixa else 0

# Exibe a média salarial da faixa etária
print(f"Média salarial da faixa etária {faixa1_user}-{faixa2_user}: {media_salarial}")
