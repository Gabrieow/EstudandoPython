'''
exercício 2:
criar uma classe chamada ContaBancaria com os atributos:
titular, saldo
com os metodos:
depositar(valor) - adicionar valor ao saldo da conta
sacar(valor) - subtrai o valor do salto da conta (n pode ficar negativo)
mostrar_saldo() - exibe o saldo da conta
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        # self.valor = 0    # aqui eu havia adicioando self.valor como atributo, porém, ele não é utilizado porque não é necessario 
                            # colocar ele dentro da classe pois nao preciso dele como instancia para armazenar valores igual no exercicio anterior.
    
    def depositar(self, valor):     # inicializo uma variavel chamada valor
        self.saldo += valor         # saldo + valor atualiza o saldo
        print(f"Deposito de R${valor} efetuado, novo saldo: R${self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:      # se o valor do saque for maior q o saldo ele nao autoriza o saque
            print("Saque não autorizado. Você não possui saldo disponível.")
        else:
            self.saldo -= valor     # se nao for maior, ta suave
            print(f"Saque de R${valor} efetuado, novo saldo: R${self.saldo}.")
    
    def mostrar_saldo(self):        # mostra o saldo
        print(f"Saldo atual: R${self.saldo}.")

pessoa1 = ContaBancaria("João da silva", 2000)

pessoa1.mostrar_saldo()
pessoa1.depositar(100)
pessoa1.sacar(2200)
