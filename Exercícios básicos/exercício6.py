def main():
    
    cotDol = float(input("Informe a cotação do dólar atual:\n"))
    reais = float(input("\nInsira o valor em reais que você deseja converter para dólar\n"))
    
    dolar = reais/cotDol
    
    print(f"\nO valor de R${reais:.2f} em dólar é de U${dolar:.2f}.")
    
