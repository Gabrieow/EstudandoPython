def main():
    
    capTanque = float(input("Informe a capacidade do tanque em litros\n"))
    litrosAbast = float(input("Informe a quantidade de litros abastecidos"))
    kmPercorrido = float(input("Informe a quilometragem percorrida desde o último abastecimento"))
    
    consumo_medio = kmPercorrido / litrosAbast
    
    autonomia_restante = consumo_medio * (capTanque - litrosAbast)
    
    print(f"\nO consumo médio do veículo é de {consumo_medio:.2f} km/l.")
    print(f"A autonomia restante do veículo é de {autonomia_restante:.2f} km.")
