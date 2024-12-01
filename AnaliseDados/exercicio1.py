with open('dados_pessoas.txt', 'r') as file:    # lê o arquivo
    linhas = file.readlines()   # lê todas as linhas do arquivo

dados = [linha.strip().split(',') for linha in linhas]  # separa uma string a cada , que tem na linha
cabecalho = dados[0] # gera o cabeçalho usando a 1 linha da variável "dados"
linhas_dados = dados[1:] # aqui não tenho certeza, mas acho ue utilizando 1: todas as linhas a partir da 1 ficam dentro da variável linhas_dados

# Exercício 1
print("Exercício 1: Exibir todos os dados")
for linha in linhas_dados:  # aqui utilizamos for pra separar string por string dentro da variável linha_dados
    print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}, Salário: {linha[3]}")  #aqui printamos cada string utilizando [], linha[0] = nome, [1] = idade e assim vai

# Exercício 2
print("\nExercício 2: Filtrar pessoas com idade maior que 30") 
for linha in linhas_dados: # mesma lógica que o de cima
    if int(linha[1]) > 30: # condicional para caso idade seja acima de 30
        print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}")   # executa a condicional printando todas as idades acima de 30

# Exercício 3
print("\nExercício 3: Estatísticas salariais")
salarios = [int(linha[3]) for linha in linhas_dados]    # inicializamos a variável salário como inteira utilizando o dado linha[3] dentro de linha in linha_dados
media_salarial = sum(salarios) / len(salarios)  # utilizamos a função sum para somar todos os salarios e len para contar quantos campos de salarios tem (5), entao pegamos o valor total e dividimos por 5
maior_salario = max(salarios)   # max é para pegar o valor máximo dentro da variável salário
menor_salario = min(salarios)   # min é pra pegar o valor mínimo dentro da variável salário
print(f"Média Salarial: {media_salarial}")  #printa os valores
print(f"Maior Salário: {maior_salario}")    #printa os valores 
print(f"Menor Salário: {menor_salario}")    #printa os valores

# Exercício 4
print("\nExercício 4: Buscar pessoas de uma cidade específica")
cidade_alvo = "São Paulo"   # inicializamos a variável cidade_alvo para conseguirmos utilizar ela dentro da condicional mais tarde
for linha in linhas_dados:  # mesma lógica que os exercícios acima
    if linha[2] == cidade_alvo:     # condicional para caso o campo 'Cidade' seja igual a variável cidade_alvo ("São Paulo")
        print(f"Nome: {linha[0]}, Idade: {linha[1]}")   # printa o cliente da cidade sp

# Exercício 5
print("\nExercício 5: Ordenar os dados por idade")
dados_ordenados = sorted(linhas_dados, key=lambda x: int(x[1]))     # sorted a gente usa pra organizar, se não me engano, lambda a gente usa como "condicional" e x: int é o valor onde começa a organização (a partir do número 1) (essa eu não tenho mt certeza, fiz por dedução)
for linha in dados_ordenados: # mesma lógica uqe os exercícios acima
    print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}, Salário: {linha[3]}")  # printa os clientes de forma ordenada a partir do sorted

# Exercício 6
print("\nExercício 6: Adicionar um novo participante")
novo_participante = "João,50,Salvador,5000\n"   # aqui a gente gera um novo dado (nome, idade, cidade, salario)
with open('dados_pessoas.txt', 'a') as file:
    file.write(novo_participante)   # aqui a gente escreve o dado dentro da file
print(f"Novo participante adicionado: {novo_participante.strip()}")     # aqui printamos o novo participante
