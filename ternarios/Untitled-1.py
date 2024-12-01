nota = int(input("Insira uma nota de 0 a 10."))

while nota < 0 or nota > 10:
    print("Valor inválido, insira novamente")
    nota = int(input("Insira uma nota de 0 a 10: "))

print("Nota válida:", nota)
