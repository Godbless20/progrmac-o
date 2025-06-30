#Construa um dicionário com as seguintes informações de alunos
#nome, número de matrícula e curso. Leia do usuário a informação de n alunos
#armazene em um vetor e imprima os dados na tela
num = int(input())
informacao = list()

for i in range(num):
    aluno = dict()
    aluno['nome'] = str(input())
    aluno['matricula'] = int(input())
    aluno['curso'] = str(input())
    informacao.append(aluno)

for c in informacao:
    print(c)
