#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo. Letras maiúsculas e minúsculas devem ser contadas juntas, e não separadamente.
nome_arquivo = str(input())
contagem =dict()
letras = "abcdefghijklmnopqrstuvwxyz"
for letra in letras:
    contagem[letra]=0

with open(nome_arquivo,'r') as arquivo:
    conteudo = arquivo.read()
    for caractere in conteudo:
        caractere = caractere.lower()
        for letra in letras:
            if caractere ==letra:
                contagem[letra] +=1
                break

for letra in letras:
    print(f'{letra}: {contagem[letra]}')


