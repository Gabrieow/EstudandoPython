'''
exercício de Associação

exercício 4:

Crie uma classe Livro com os atributos:
titulo, autor, ano_publicacao e disponivel (se o livro ta disponivel ou emprestado)

crie uma classe Biblioteca que tenha os metodos:
adicionar_livro(Livro) - adiciona um livro à biblioteca
emprestar_livro(titulo) - empresta um livro à biblioteca, mudando o status pra indisponivel
devolver_livro(titulo) - devolve um livro à biblioteca, mudando o status pra dispnivel
listar_livros() - listar todos os livros na biblioteca e o seu status
'''

class Livro:    # Criando classe livro
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True      # aqui a gnt define disponivel como bool pq mais tarde a gente usa condicional

    def emprestar(self):
        if self.disponivel:     # se tá disponivel
            self.disponivel = False     # a gente empresta e define ele como indisponivel
            print(f'O livro "{self.titulo}" foi emprestado.')   # e dps exibe msg falando q foi emprestado
        else:
            print(f'O livro "{self.titulo}" não está disponível.')  # se nao esta disponivel a gnt exibe msg dizendo q nao ta disponivel

    def devolver(self):
        if not self.disponivel: # se nao esta disponivel
            self.disponivel = True  # a gente devolve e define ele como disponivel
            print(f'O livro "{self.titulo}" foi devolvido.')    # e exibe msg falando q foi devolvido
        else:
            print(f'O livro "{self.titulo}" não foi emprestado, não há como devolver.')   # se ja estiver disponivel a gnt exibe aviso
    
class Biblioteca:
    def __init__(self):
        self.biblioteca_livros = []     # aq a gnt cria uma lista pra armazenar todos os livros que irão ser adicionados

    def adicionar_livro(self, livro):
        self.biblioteca_livros.append(livro)    # aq a gnt usa append pra adicionar os livros na biblioteca_livros
    
    def emprestar_livro(self, titulo):
        for livro in self.biblioteca_livros:    # aq a gnt cria uma variavel pra cada livro dentro da lista
            if livro.titulo == titulo:  # se o titulo do livro for igual ao titulo inserido pelo usuario
                livro.emprestar()   # a gnt chama a função da classe Livro e empresta
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')  # se nao for encontrado no laço de repetiçao, a gnt emite aviso falando q nao achamo
    
    def devolver_livro(self, titulo):
        for livro in self.biblioteca_livros:    # novamente criando uma variavel dentro da lista
            if livro.titulo == titulo:  # mesma logica do codigo acima mas pra devolver
                livro.devolver()
                return
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')
    
    def listar_livros(self):
        print("Livros na biblioteca:")
        for livro in self.biblioteca_livros:    # aq a gnt chama mais um laço de repeticao
            status = "Disponível" if livro.disponivel else "Indisponível"   # definimos uma variavel status = "disponível" pra caso a bool livro.disponivel esteja True e caso não esteja, ela vira "Indisponível"
            print(f' - {livro.titulo} ({livro.autor}, {livro.ano_publicacao}) - {status}')  # exibe o livro
    
livro1 = Livro("A cor que caiu do espaço", "H.P. Lovecraft", 1927)
livro2 = Livro("O chamado de Cthulhu", "H.P. Lovecraft", 1928)      # adicionei 3 livros na classe livro
livro3 = Livro("A Música de Erich Zann", "H.P. Lovecraft", 1922)

biblioteca = Biblioteca()   # criei uma variavel pra usar a classe biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)  # inseri os 3 livros na biblioteca
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()
biblioteca.emprestar_livro("A cor que caiu do espaço")  # emprestei
biblioteca.listar_livros()
biblioteca.devolver_livro("A cor que caiu do espaço")   # devolvi
biblioteca.listar_livros()
biblioteca.emprestar_livro("O corvo")   # exibiu mensagem falando que o livro nao foi encontrado pq eu nao adicionei ele