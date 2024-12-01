
def main():
    
    saque = int(input("Digite o valor do saque:\n"))
    
    n100 = saque // 100
    saque = saque % 100
    
    n50 = saque // 50
    saque = saque % 50
    
    n20 = saque // 20
    saque = saque %20
    
    n10 = saque // 10
    saque = saque %10
    
    n5 = saque // 5
    saque = saque %5
    
    print(f"Cédulas de 100: {n100}")
    print(f"Cédulas de 50: {n50}")
    print(f"Cédulas de 20: {n20}")
    print(f"Cédulas de 10: {n10}")
    print(f"Cédulas de 5: {n5}")
    


if __name__ == "__main__":
        main()