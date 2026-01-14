#2. Gerenciamento de Usuários
#Cadastro de usuários com os atributos:/
#Nome (string)
#E-mail (string)
#Número de matrícula (string)
#Tipo de usuário (Estudante ou Professor)
#Diferenciar usuários por tipo:
#Estudantes: podem pegar até 3 livros emprestados.
#Professores: podem pegar até 5 livros emprestados.

class Usuario:
    def __init__ (self, nome, email, matricula, cargo):
        self.nome = nome
        self.email = email
        self.matricula = matricula
        self.cargo = cargo
        self.limite_emprestimos = 3 if cargo == "estudante" else 5
        
def
        
        