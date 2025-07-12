#Faça um programa que leia os dados de 10 alunos (Nome, matricula, Média Final), armazenando em um vetor. Uma vez lidos os dados, divida estes dados em 2 novos vetores, o vetor dos aprovados e o vetor dos reprovados, considerando a média mínima para a aprovação como sendo 5.0. Exibir na tela os dados do vetor de aprovados, seguido dos dados do vetor de reprovados
vetor=list()
for i in range(10):
    aluno = dict()
    aluno['nome'] = str(input())
    aluno['matricula'] = int(input())
    aluno['media'] = float(input())
    vetor.append(aluno)
vet_aprovados = list()
vet_reprovados = list()
for aluno in vetor:
    if aluno['media'] >= 5.0:
        vet_aprovados.append(aluno)
    else:
        vet_reprovados.append(aluno)
for aprovado in vet_aprovados:
    print(aprovado)
for reprovado in vet_reprovados:
    print(reprovado)
