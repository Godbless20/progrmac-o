#Faça um programa que realize a leitura dos seguintes dados relativos a um conjunto de alunos: Matricula, Nome, Código da Disciplina, Nota1 e Nota2. O tamanho da turma deve ser dado pelo usuário. Após ler todos os dados digitados, e depois de armazená-los em um vetor de dicionários, exiba na tela a listagem final dos alunos com as suas respectivas médias finais (use uma média ponderada: Nota1 com peso=1.0 e Nota2 com peso=2.0). Para cada aluno, inclua a média no dicionário.
num = int(input())
conjunto_de_aluno = []
for i in range(num):
    aluno=dict()
    aluno['matricula'] = int(input())
    aluno['nome']=str(input())
    aluno['codigo'] = str(input())
    aluno['nota1'] = float(input())
    aluno['nota2'] = float(input())
    aluno['media'] = (aluno['nota1']*1.0 + aluno['nota2']*2.0)/3.0
    conjunto_de_aluno.append(aluno)
for aluno in conjunto_de_aluno:
    print(aluno)