def main():
    
    kmPercorrido = float(input("Informe o valor de KM percorridos:\n"))
    dias = float(input("\nInforme a quantidade de dias que foi locado:\n"))
    
    kmpre�o = kmPercorrido*0.70
    diaspre�o = dias*70 
    somafinal = kmpre�o+diaspre�o 
    
    print(f"\nO valor total pelos kms percorridos foi de R${kmpre�o:.2f}.\n")
    print(f"\nO valor total pelos dias locados foi de R${diaspre�o:.2f}\n")
    print(f"\nO valor total da loca��o foi de R${somafinal:.2f}.")
    
        
def main():
    valorgasto = float(input("Informe o valor gasto no restaurante:\n"))
    
    comissao = valorgasto*0.1
    valortotal = comissao+valorgasto
    
    print(f"O valor total ser� de R${valortotal:.2f}. Sendo R${comissao:.2f} da comiss�o de 10% do gar�om.")