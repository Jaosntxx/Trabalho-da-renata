from abc import ABC, abstractmethod

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, codigo):
        # Encapsulamento: atributos protegidos
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._codigo = codigo

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def codigo(self):
        return self._codigo

    def __str__(self):
        return f"[{self._codigo}] {self._titulo} - {self._autor} ({self._ano_publicacao})"


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
        """Polimorfismo: cada subclasse define seu limite."""
        pass

    def emprestar_livro(self, livro):
        if len(self._livros_emprestados) >= self.limite_emprestimos:
            print(f"{self._nome} atingiu o limite de {self.limite_emprestimos} livros.")
            return False
        
        self._livros_emprestados.append(livro)
        print(f"Livro '{livro.titulo}' emprestado para {self._nome}.")
        return True

    def listar_emprestimos(self):
        print(f"\nLivros emprestados para {self._nome}:")
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
        # Pré-cadastrar livros
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
        # print(f"Livro '{titulo}' cadastrado com sucesso")

    def listar_livros(self):
        print("\n--- Todos os Livros Disponíveis ---")
        if not self._tdlivros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self._tdlivros:
            print(livro)

    def buscar_livro_por_codigo(self, codigo):
        for livro in self._tdlivros:
            if livro.codigo == codigo:
                return livro
        return None


