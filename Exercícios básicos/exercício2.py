def main():
    
    horas = float(input("Digite o valor das horas:\n")) ## Não é necessário colocar o 'f' após o input se o valor não for caractere.
    minutos = float(input("\nDigite o valor de minutos:\n"))
    segundos = float(input("\nDigite o valor dos segundos:\n"))

    resultadofinal = horas*3600+minutos*60+segundos
    
    print(f"O total de segundos de {horas}h {minutos}min {segundos}seg é de {resultadofinal}seg.")
    