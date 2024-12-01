populacaoA = int(input("Insira o tamanho da populaçãoA: "))
populacaoB = int(input("Insira o tamanho da populaçãoB: "))
crescimentoA = int(input("Insira o crescimento da população A: "))
crescimentoB = int(input("Insira o crescimento da população B: "))
anos = 0

if populacaoA < populacaoB:
    while populacaoA < populacaoB:
        populacaoA += populacaoA * crescimentoA/100
        populacaoB += populacaoB * crescimentoB/100
        anos += 1

    print(f"PopulaçãoA passou populaçãoB em {anos}")

else:
    while populacaoA > populacaoB:
        populacaoA += populacaoA * crescimentoA/100
        populacaoB += populacaoB * crescimentoB/100
        anos+=1
        
    print(f"PopulaçãoB passou populaçãoA em {anos}")


