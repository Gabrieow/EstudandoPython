def main():
    
    cotDol = float(input("Informe a cota��o do d�lar atual:\n"))
    reais = float(input("\nInsira o valor em reais que voc� deseja converter para d�lar\n"))
    
    dolar = reais/cotDol
    
    print(f"\nO valor de R${reais:.2f} em d�lar � de U${dolar:.2f}.")
    
