class Aluno:
    def __init__(self, nome_aluno, curso, nota_final):
        self.nome_aluno = nome_aluno
        self.curso = curso
        self.nota_final = nota_final

    def status(self):
        print(f"Nome do Aluno: {self.nome_aluno} \nCurso: {self.curso} \nNota Final: {self.nota_final}")
        if self.nota_final > 7:
            print(f"Parabéns {self.nome_aluno}! Você está aprovado(a).")
        else:
            print(f"Que pena {self.nome_aluno}! Você está reprovado.")

aluno1 = Aluno("Júlia Alves", "SQL Básico", 10)
aluno2 = Aluno("Kaique Gabriel", "TI", 8)
aluno3 = Aluno("Gabriela Santos", "Python Básico", 4)

aluno1.status()
aluno2.status()
aluno3.status()