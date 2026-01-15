from usuarios import (
    cadastrar_usuario,
    listar_usuarios,
    emprestar_livro,
    devolver_livro
)
#definir constante para matrícula do administrador
MATRICULA_ADMIN = "000000"

#criaçao de todos os menus do sistema
menu_inicial = [
    "menu administrador",
    "menu usuario",
    "sair"
]
#somente para o administrador/bibliotecario com a matricula especiol
menu_adm = [
    "listar livros",
    "cadastrar livro",
    "remover livro",
    "listar emprestimos",
    "cadastrar usuario",
    "remover usuario",
    "listar usuarios",
    "voltar"
]

#menu de estudantes e professores
menu_user = [
    "listar livros",
    "emprestimo de livro",
    "devolucao de livro",
    "meus emprestimos",
    "voltar"
]

#criação de função para mostrar os menus e qual menu vai aparecer
def mostrar_menu(menu):
    for i, opcao in enumerate(menu, start=1):
        print(f"{i} - {opcao}")

while True:
    print("\n=== MENU INICIAL ===")
    mostrar_menu(menu_inicial)

    opcao = input("Escolha uma opção: ")
#inserção de credenciais para o administrador
    if opcao == "1":
        matricula = input("Digite a matrícula do administrador: ")
#verificação da matricula
        if matricula == MATRICULA_ADMIN:
            while True:
                #abertura do menu do administrador
                print("\n=== MENU ADMINISTRADOR ===")
                mostrar_menu(menu_adm)

                op_adm = input("Escolha uma opção: ")

                if op_adm == "7":  # voltar
                    break
                else:
                    print("Função ainda não implementada.")

        else:
            print("Acesso negado! Matrícula inválida.")

    elif opcao == "2":
        while True:
            print("\n=== MENU USUÁRIO ===")
            mostrar_menu(menu_user)

            op_user = input("Escolha uma opção: ")

            if op_user == "5":  # voltar
                break
            else:
                print("Função ainda não implementada.")

    elif opcao == "3":
        print(" Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
#inicialização das funções dos menus de usuário
def mostrar_menu_user(menu_user):
    for i, opc in enumerate(menu_user, start=1):
        print(f"{i} - {opc}")

def menu_usuario():
    while True:
        print("\n=== MENU DE USUARIOS ===")
        mostrar_menu(menu_user)
    
        opc = input("Escolha uma opção: ")
    
        if opc == "1":
            print(lista_de_livros())
        elif opc == "2":
            emprestar_livro()
            if livro == emprestado:
                print("Livro emprestado com sucesso")
                lista_de_livros.remove(livro)
            else:
                print("Livro ja foi emprestado")
        elif opc == "3":
            devolver_livro()
            if livro == devolvido:
                print("Livro devolvido com sucesso")
                lista_de_livros.append(livro)
        elif opc == "4":
            listar_meus_emprestimos()
        elif opc == "5":
            break
        else:
            print("Opção inválida!")
#menu de administrador com suas funções
def mostrar_menu_adim(menu_adm):
    for i, opc in enumerate(menu_adm, start=1):
        print(f"{i} - {opc}")

def menu_admin():
    while True:
        print("\n=== MENU ADMINISTRADOR ===")
        mostrar_menu(menu_adm)

        opc = input("Escolha uma opção: ")
        
        if opc == "1":
            print(lista_de_livros())
        elif opc == "2": 
            cadastrar_livro()
        elif opc == "3":
            remover_livro()
        elif opc == "4":
            listar_emprestimos()
        elif opc == "5":
            cadastrar_usuario()
        elif opc == "6":
            remover_usuario()
        elif opc == "7":
            listar_usuarios()

        if opc == "8":  # voltar
            break
        else:
            print("Função ainda não implementada.")