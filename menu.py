from biblioteca import GerenciamentoLivros
from usuarios import (cadastrar_usuario, listar_usuarios, remover_usuario, 
                      buscar_usuario, listar_todos_emprestimos)

# Constante para matrícula do administrador
MATRICULA_ADMIN = "000000"

# Instância global de gerenciamento de livros
gerenciamento_livros = GerenciamentoLivros()

# Criação de todos os menus do sistema
menu_inicial = [
    "menu administrador",
    "menu usuario",
    "sair"
]

menu_adm = [
    "listar livros",
    "cadastrar livro",
    "pesquisar livro",
    "listar emprestimos de todos usuarios",
    "cadastrar usuario",
    "remover usuario",
    "listar usuarios",
    "voltar"
]

menu_user = [
    "listar livros",
    "pesquisar livro",
    "emprestimo de livro",
    "devolucao de livro",
    "meus emprestimos",
    "voltar"
]

def mostrar_menu(menu):
    """Exibe o menu formatado"""
    for i, opcao in enumerate(menu, start=1):
        print(f"{i} - {opcao}")

def cadastrar_livro():
    """Cadastra um novo livro no sistema"""
    print("\n=== CADASTRAR LIVRO ===")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    codigo = input("Código do livro: ")
    
    try:
        ano = int(ano)
        gerenciamento_livros.cad_li(titulo, autor, ano, codigo)
        print(f"Livro '{titulo}' cadastrado com sucesso!")
    except ValueError:
        print("Erro: Ano inválido!")

def buscar_livro_por_codigo(codigo):
    """Busca um livro pelo código"""
    for livro in gerenciamento_livros._tdlivros:
        if livro.codigo == codigo:
            return livro
    return None

def menu_administrador():
    """Menu do administrador"""
    while True:
        print("\n=== MENU ADMINISTRADOR ===")
        mostrar_menu(menu_adm)

        op_adm = input("Escolha uma opção: ")
        
        if op_adm == "1":
            gerenciamento_livros.listar_livros()
        elif op_adm == "2":
            cadastrar_livro()
        elif op_adm == "3":
            termo = input("Digite o termo de pesquisa: ")
            gerenciamento_livros.pesquisar_livro(termo)
        elif op_adm == "4":
            listar_todos_emprestimos()
        elif op_adm == "5":
            cadastrar_usuario()
        elif op_adm == "6":
            remover_usuario()
        elif op_adm == "7":
            listar_usuarios()
        elif op_adm == "8":
            break
        else:
            print("Opção inválida!")

def menu_usuario(usuario):
    """Menu do usuário (estudante ou professor)"""
    while True:
        print(f"\n=== MENU USUÁRIO - {usuario.nome} ===")
        mostrar_menu(menu_user)

        op_user = input("Escolha uma opção: ")
        
        if op_user == "1":
            gerenciamento_livros.listar_livros()
        elif op_user == "2":
            termo = input("Digite o termo de pesquisa: ")
            gerenciamento_livros.pesquisar_livro(termo)
        elif op_user == "3":
            codigo = input("Digite o código do livro para emprestar: ")
            livro = buscar_livro_por_codigo(codigo)
            if livro:
                usuario.emprestar_livro(livro)
            else:
                print(f"Livro com código '{codigo}' não encontrado.")
        elif op_user == "4":
            codigo = input("Digite o código do livro para devolver: ")
            livro = buscar_livro_por_codigo(codigo)
            if livro:
                usuario.devolver_livro(livro)
            else:
                print(f"Livro com código '{codigo}' não encontrado.")
        elif op_user == "5":
            usuario.listar_emprestimos()
        elif op_user == "6":
            break
        else:
            print("Opção inválida!")

def main():
    """Função principal do sistema"""
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        mostrar_menu(menu_inicial)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            matricula = input("Digite a matrícula do administrador: ")
            if matricula == MATRICULA_ADMIN:
                menu_administrador()
            else:
                print("Acesso negado! Matrícula inválida.")

        elif opcao == "2":
            matricula = input("Digite sua matrícula: ")
            usuario = buscar_usuario(matricula)
            if usuario:
                menu_usuario(usuario)
            else:
                print("Usuário não encontrado! Solicite cadastro ao administrador.")

        elif opcao == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()