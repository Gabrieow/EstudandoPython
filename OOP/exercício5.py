'''
exercicio de Composição

Exercício 5: 

Crie uma classe Produto com os atributos:
nome, preço, quantidade

Crie uma classe CarrinhoDeCompras com os métodos:
adicionar_produto(produto): adiciona um produto ao carrinho.
remover_produto(produto): remove um produto do carrinho.
calcular_total(): calcula o valor total (preço x quantidade de cada produto).
listar_produtos(): exibe todos os produtos no carrinho.
'''

class Produto:  # criando classe produto
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class CarrinhoDeCompras:    # criando classe carrinho
    def __init__(self):
        self.carrinho = []  # criando lista carrinho pra por os produtos

    def adicionar_produto(self, produto):
        self.carrinho.append(produto)   # adicionando produtos no carrinho
    
    def remover_produto(self, produto):
        self.carrinho.remove(produto)   # removendo produtos do carrinho
    
    def calcular_total(self):
        valor_total = 0     # definindo variavel antes de iniciar o laço de repetiçao
        for produto in self.carrinho:   # iniciando laço
            valor_total += produto.preco * produto.quantidade   # atualizando variavel conforme preço e quantidade do produto que vai lendo de linha em linha
        print(f"O valor total foi de R${valor_total}.")     # mostra o calculo
    
    def listar_produtos(self):
        for produto in self.carrinho:   # laço de repetição pra mostrar todos os produtos do carrinho
            print(f"Nome: {produto.nome}\nPreço: {produto.preco}\nQuantidade: {produto.quantidade}\n\n")

produto1 = Produto("Feijão", 20, 1)
produto2 = Produto("Arroz", 30, 2)      # criando os produtos
produto3 = Produto("Macarrão", 15, 1)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)    # adicionando os produtos no carrinho
carrinho.adicionar_produto(produto3)
carrinho.listar_produtos()      # listando os produtos
carrinho.remover_produto(produto3)  # removendo um produto
carrinho.listar_produtos()
carrinho.calcular_total()   # fazendo o calculo total dos produtos no carrinho