#Crie um dicionário representando os alunos de um determinado curso. O dicionário deve conter a matrícula do aluno, nome, nota da primeira prova, nota da segunda prova e nota da terceira prova.
#Permita ao usuário entrar com os dados de 5 alunos.
#Encontre o aluno com maior nota da primeira prova.
#Encontre o aluno com maior média geral.
#Encontre o aluno com menor média geral.
#Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 7 para aprovação.
informacao=list()
soma=[]
for i in range(5):
    aluno=dict()
    aluno['matricula']=int(input())
    aluno['nome']=str(input())
    aluno['nota1']=float(input())
    aluno['nota2'] = float(input())
    aluno['nota3'] = float(input())
    aluno['media'] =(aluno['nota1']+aluno['nota2']+aluno['nota3'])/3
    informacao.append(aluno)
maior_nota1 = 0
maior_media=0
menor_media=informacao[0]['media']
nome_aluno=''
aluno_maior_media =''
aluno_menor_media=informacao[0]['nome']
for i in range(len(informacao)):
    if informacao[i]['nota1'] > maior_nota1:
        maior_nota1=informacao[i]['nota1']
        nome_aluno = informacao[i]['nome']
    if informacao[i]['media']>maior_media:
        maior_media=informacao[i]['media']
        aluno_maior_media=informacao[i]['nome']
    if informacao[i]['media']<menor_media:
        menor_media=informacao[i]['media']
        aluno_menor_media=informacao[i]['nome']
print(f'Aluno {nome_aluno} tem a maior nota1: {maior_nota1:.2f}')
print(f'Aluno {aluno_maior_media} tem a maior media: {maior_media:.2f}')
print(f'Aluno {aluno_menor_media} tem a menor media: {menor_media:.2f}')
for i in range(len(informacao)):
    if informacao[i]['media']>=7:
        print(f'Aluno {informacao[i]["nome"]} esta aprovado com media {informacao[i]["media"]:.2f}')
    elif informacao[i]['media'] <7:
        print(f'Aluno {informacao[i]["nome"]} esta reprovado com media {informacao[i]["media"]:.2f}')





