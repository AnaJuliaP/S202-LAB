class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} esta ministrando uma aula sobre {assunto}.')

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f'O aluno {self.nome} esta presente.'

class Aula:
    def __init__(self, professor, assunto):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []
        
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        presenca_alunos = "\n".join([aluno.presenca() for aluno in self.alunos])
        return f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}: \n {presenca_alunos}.'


professor = Professor("Joao")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Ana")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())