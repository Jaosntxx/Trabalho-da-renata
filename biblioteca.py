#coisar a classe abstrata da herança
from abc import ABC, abstractmethod

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, codigo):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._codigo = codigo
        self._disponivel = True  #controlar disponibilidade

    @property
    def titulo(self):
        return self._titulo
    @property
    def autor(self):
        return self._autor
    @property
    def codigo(self):
        return self._codigo
    @property
    def disponivel(self):
        return self._disponivel
    #ja atualiza a disponibilidade do livro, se estiver disponivel,
    #  empresta depois ele fica indisponivel
    def emprestar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False
    #quando devolve deixa disponivel de novo 
    def devolver(self):
        self._disponivel = True
    #mostrar bonitinho 
    def __str__(self):
        status = "Disponível" if self._disponivel else "Indisponível"
        return f"[{self._codigo}] {self._titulo} - {self._autor} ({self._ano_publicacao}) [{status}]"

#classe abstrata
class Usuario(ABC):
    def __init__(self, nome, email, matricula):
        # Encapsulamento
        self._nome = nome
        self._email = email
        self._matricula = matricula
        # Associação: Lista de objetos Livro
        self._livros_emprestados = []

    @property
    def nome(self):
        return self._nome
    @property
    @abstractmethod
    def limite_emprestimos(self):
        """as classes herdeiras que sabem seu limite de emprestimos"""
        pass

    def emprestar_livro(self, livro):
        if len(self._livros_emprestados) >= self.limite_emprestimos:
            print(f"Erro: {self._nome} atingiu o limite de {self.limite_emprestimos} livros.")
            return False
        
        if not livro.disponivel:
            print(f"Erro: O livro '{livro.titulo}' não está disponível.")
            return False

        if livro.emprestar():
            self._livros_emprestados.append(livro)
            print(f"Sucesso: Livro '{livro.titulo}' emprestado para {self._nome}.")
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self._livros_emprestados:
            livro.devolver()
            self._livros_emprestados.remove(livro)
            print(f"Sucesso: Livro '{livro.titulo}' devolvido por {self._nome}.")
        else:
            print(f"Erro: {self._nome} não possui o livro '{livro.titulo}'.")

    def listar_emprestimos(self):
        print(f"Livros emprestados para {self._nome}:")
        if not self._livros_emprestados:
            print("Nenhum livro emprestado.")
        else:
            for livro in self._livros_emprestados:
                print(f"- {livro}")

class Estudante(Usuario):
    @property
    def limite_emprestimos(self):
        # Polimorfismo
        return 3

class Professor(Usuario):
    @property
    def limite_emprestimos(self):
        # Polimorfismo
        return 5


class GerenciamentoLivros:
    def __init__(self):
        self._tdlivros = []
        self._livros_por_autor = {}
        # Pré-cadastrar livros pra ser rápido
        self.cad_li("Dom Quixote", "Miguel de Cervantes", 1605, "L001")
        self.cad_li("1984", "George Orwell", 1949, "L002")
        self.cad_li("A Revolução dos Bichos", "George Orwell", 1945, "L003")
        self.cad_li("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "L004")
        self.cad_li("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "L005")

    def cad_li(self, titulo, autor, ano_publicacao, codigo):
        for livro in self._tdlivros:
            if livro.codigo == codigo:
                print(f"Livro com código '{codigo}' já cadastrado.")
                return
        
        novo_livro = Livro(titulo, autor, ano_publicacao, codigo)
        self._tdlivros.append(novo_livro)
        
        if autor not in self._livros_por_autor:
            self._livros_por_autor[autor] = []
        self._livros_por_autor[autor].append(novo_livro)
#lista todos os livros e pode listar por autor
    def listar_livros(self):
        print("os Livros Disponíveis no momento")
        if not self._tdlivros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self._tdlivros:
            print(livro)
            
        opcao = input("Deseja listar livros de um autor específico? (s/n): ")
        if opcao.lower() == 's':
            autor = input("Digite o nome do autor: ")
            if autor in self._livros_por_autor:
                print(f" Livros do {autor}")
                for livro in self._livros_por_autor[autor]:
                    print(livro)
            else:
                print(f"Autor '{autor}' não encontrado.")

    def pesquisar_livro(self, termo):
        print(f" Resultados da Pesquisa para: {termo}")
        resultados = []   
        for livro in self._tdlivros:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower():
                resultados.append(livro)
        
        if resultados:
            for livro in resultados:
                print(livro)
            print(f"Total: {len(resultados)} livro encontrado")
        else:
            print("Nenhum livro encontrado.")