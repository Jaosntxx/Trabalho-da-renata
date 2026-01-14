class Livro:
    def __init__(self, titulo, autor, ano_publicacao, codigo):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.codigo = codigo
    def __str__(self):
        return f"[{self.codigo}] {self.titulo} - {self.autor} ({self.ano_publicacao})"

class GerenciamentoLivros:
    def __init__(self):
        self.tdlivros = []
        self.livros_por_autor = {}
        # Pré-cadastrar livros,ser rapido
        self.cad_li("Dom Quixote", "Miguel de Cervantes", 1605, "L001")
        self.cad_li("1984", "George Orwell", 1949, "L002")
        self.cad_li("A Revolução dos Bichos", "George Orwell", 1945, "L003")
        self.cad_li("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "L004")
        self.cad_li("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "L005")
    def cad_li(self, titulo, autor, ano_publicacao, codigo):
        # olhar se já tem algum livro com mesmo código
        for livro in self.tdlivros:
            if livro.codigo == codigo:
                print(f"Livro com código '{codigo}' já cadastrado.")
                return
        #novo livro
        novo_livro = Livro(titulo, autor, ano_publicacao, codigo)
        self.tdlivros.append(novo_livro)
        # Add ao dicionário de autores se não existir
        if autor not in self.livros_por_autor:
            self.livros_por_autor[autor] = []
        self.livros_por_autor[autor].append(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso")

    def listar_livros(self):
        print("\n--- Todos os Livros Disponíveis ---")
        if not self.tdlivros:
            print("Nenhum livro cadastrado.")
            return
        for livro in self.tdlivros:
            print(livro)

    def pesquisar_livro(self, termo):
        print(f"\n--- Resultados da Pesquisa para: '{termo}' ---")
        resultados = []   
        # Primeiro tenta buscar direto no dicionário de autores (busca exata)
        if termo in self.livros_por_autor:
            resultados = self.livros_por_autor[termo]
        else:
            # Se não encontrar, procura nos outros livros
            for livro in self.tdlivros:
                if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower():
                    resultados.append(livro)
        
        if resultados:
            for livro in resultados:
                print(livro)
            print(f"\nTotal: {len(resultados)} livro(s) encontrado(s)")
        else:
            print("Nenhum livro encontrado.")
if __name__ == "__main__":
    sistema = GerenciamentoLivros()