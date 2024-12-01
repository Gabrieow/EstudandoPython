def main():
    
    kmPercorrido = float(input("Informe o valor de KM percorridos:\n"))
    dias = float(input("\nInforme a quantidade de dias que foi locado:\n"))
    
    kmpreço = kmPercorrido*0.70
    diaspreço = dias*70 
    somafinal = kmpreço+diaspreço 
    
    print(f"\nO valor total pelos kms percorridos foi de R${kmpreço:.2f}.\n")
    print(f"\nO valor total pelos dias locados foi de R${diaspreço:.2f}\n")
    print(f"\nO valor total da locação foi de R${somafinal:.2f}.")
    
        
