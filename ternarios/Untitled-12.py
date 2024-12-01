populacaoA = 80000
populacaoB = 200000
anos = 0

while populacaoA < populacaoB:
    populacaoA += populacaoA * 0.03
    populacaoB += populacaoB * 0.015
    anos += 1

print(f"PopulaçãoA passou a população de PopulaçãoB em {anos}.\nTotal populaçãoA: {populacaoA}\nTotal populaçãoB: {populacaoB}")
