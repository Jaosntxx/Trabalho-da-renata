class Usuario:
    def __init__(self, nome, email, matricula, cargo):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.cargo = cargo

        self.limite_emprestimos = 3 if cargo == "estudante" else 5
        self.livros_emprestados = 0
        self.devedor = False



usuarios = []

def cadastrar_usuario():
    nome = input("Nome: ")
    email = input("E-mail: ")
    matricula = input("Matrícula: ")
    cargo = input("Cargo (estudante/professor): ")

    usuario = Usuario(nome, email, matricula, cargo)
    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        restantes = usuario.limite_emprestimos - usuario.livros_emprestados
        status = "DEVENDO LIVRO" if usuario.devedor else "OK"

        print(f"""
Nome: {usuario.nome}
E-mail: {usuario.email}
Matrícula: {usuario.matricula}
Cargo: {usuario.cargo}
Livros emprestados: {usuario.livros_emprestados}
Pode pegar ainda: {restantes}
Status: {status}
---------------------------
""")

print(cadastrar_usuario())