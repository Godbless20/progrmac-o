#Utilizando um dicionário, faça um programa que permita a entrada de nome, endereço e telefone de 5 pessoas e os imprima em ordem alfabética.
lista=list()
for i in range(5):
    pessoa=dict()
    pessoa['nome']=str(input())
    pessoa['endereco'] = str(input())
    pessoa['telefone'] = str(input(''))
    lista.append(pessoa)
for i in range(len(lista)-1):
    for j in range(len(lista)-1-i):
        if lista[j]['nome'].lower() > lista[j+1]['nome'].lower():
            aux =lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux

for pessoa in lista:
    print(pessoa)