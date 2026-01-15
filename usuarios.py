from biblioteca import Estudante, Professor

# Dicionário global para armazenar usuários cadastrados
usuarios_cadastrados = {}

def cadastrar_usuario():
    """Cadastra um novo usuário (Estudante ou Professor)"""
    print("\n=== CADASTRAR USUÁRIO ===")
    nome = input("Nome: ")
    email = input("Email: ")
    matricula = input("Matrícula: ")
    
    if matricula in usuarios_cadastrados:
        print(f"Erro: Usuário com matrícula '{matricula}' já cadastrado.")
        return
    
    tipo = input("Tipo (1-Estudante / 2-Professor): ")
    
    if tipo == "1":
        usuarios_cadastrados[matricula] = Estudante(nome, email, matricula)
        print(f"Estudante '{nome}' cadastrado com sucesso!")
    elif tipo == "2":
        usuarios_cadastrados[matricula] = Professor(nome, email, matricula)
        print(f"Professor '{nome}' cadastrado com sucesso!")
    else:
        print("Tipo inválido!")

def listar_usuarios():
    """Lista todos os usuários cadastrados"""
    print("\n=== USUÁRIOS CADASTRADOS ===")
    if not usuarios_cadastrados:
        print("Nenhum usuário cadastrado.")
        return
    
    for matricula, usuario in usuarios_cadastrados.items():
        tipo = "Estudante" if isinstance(usuario, Estudante) else "Professor"
        print(f"[{matricula}] {usuario.nome} - {tipo} (Limite: {usuario.limite_emprestimos} livros)")

def remover_usuario():
    """Remove um usuário do sistema"""
    print("\n=== REMOVER USUÁRIO ===")
    matricula = input("Digite a matrícula do usuário a remover: ")
    
    if matricula in usuarios_cadastrados:
        usuario = usuarios_cadastrados[matricula]
        if usuario._livros_emprestados:
            print(f"Erro: {usuario.nome} possui livros emprestados. Devolva-os antes de remover.")
        else:
            del usuarios_cadastrados[matricula]
            print(f"Usuário '{usuario.nome}' removido com sucesso!")
    else:
        print(f"Usuário com matrícula '{matricula}' não encontrado.")

def buscar_usuario(matricula):
    """Busca um usuário pela matrícula"""
    return usuarios_cadastrados.get(matricula)

def listar_todos_emprestimos():
    """Lista todos os empréstimos de todos os usuários"""
    print("\n=== EMPRÉSTIMOS DE TODOS OS USUÁRIOS ===")
    if not usuarios_cadastrados:
        print("Nenhum usuário cadastrado.")
        return
    
    tem_emprestimo = False
    for usuario in usuarios_cadastrados.values():
        if usuario._livros_emprestados:
            tem_emprestimo = True
            usuario.listar_emprestimos()
            print()
    
    if not tem_emprestimo:
        print("Nenhum empréstimo ativo no momento.")