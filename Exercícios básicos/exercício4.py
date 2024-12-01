def main():
    
    nota1 = float(input("Digite o valor da sua primeira nota:\n"))
    nota2 = float(input("Digite o valor da sua segunda nota:\n"))
    nota3 = float(input("Digite o valor da usa terceira nota:\n"))
    
    media = (nota1*2+nota2*3+nota3*5)/(2+3+5)
    
    print(f"O valor da média final é {media:.2f}.") ## Colocando ":.2f" o código limita a duas casas decimais após o . para melhor visualização da nota.
    
    
