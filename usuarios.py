
class Usuario:
    def __init__ (self, nome, email, matricula, cargo,verif_matricula=000000):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.cargo = cargo
        self.limite_emprestimos = 3 if cargo == "estudante" else 5    

def cadastrar_usuario(nome, email, matricula, cargo):
    novo_usuario = Usuario(nome, email, matricula, cargo)
    return novo_usuario
def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario.nome}, E-mail: {usuario.email}, Matrícula: {usuario.matricula}, Tipo: {usuario.cargo}, Limite de Empréstimos: {usuario.limite_emprestimos}")
        
nome = input("Digite o nome do usuário: ")
email = input("Digite o e-mail do usuário: ")
matricula = input("Digite a matrícula do usuário: ")
cargo = input("Digite o tipo de usuário (estudante/professor): ")
usuario = cadastrar_usuario(nome, email, matricula, cargo) 

