MATRICULA_ADMIN = "000000"

menu_inicial = [
    "menu administrador",
    "menu usuario",
    "sair"
]

menu_adm = [
    "listar livros",
    "cadastrar livro",
    "remover livro",
    "listar emprestimos",
    "cadastrar usuario",
    "remover usuario",
    "voltar"
]

menu_user = [
    "listar livros",
    "emprestimo de livro",
    "devolucao de livro",
    "meus emprestimos",
    "voltar"
]

def mostrar_menu(menu):
    for i, opcao in enumerate(menu, start=1):
        print(f"{i} - {opcao}")

while True:
    print("\n=== MENU INICIAL ===")
    mostrar_menu(menu_inicial)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        matricula = input("Digite a matrícula do administrador: ")

        if matricula == MATRICULA_ADMIN:
            while True:
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
        print("👋 Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
