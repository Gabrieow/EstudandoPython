def main():
    
    horas = float(input("Digite o valor das horas:\n")) ## N�o � necess�rio colocar o 'f' ap�s o input se o valor n�o for caractere.
    minutos = float(input("\nDigite o valor de minutos:\n"))
    segundos = float(input("\nDigite o valor dos segundos:\n"))

    resultadofinal = horas*3600+minutos*60+segundos
    
    print(f"O total de segundos de {horas}h {minutos}min {segundos}seg � de {resultadofinal}seg.")
    