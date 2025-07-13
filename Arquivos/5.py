#Faça um programa que receba do usuário um arquivo texto e um caractere. Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.
nome_arquivo = str(input())
caractere = str(input())
cont =0
with open(nome_arquivo,'r') as arquivo:
    linhas=arquivo.readlines()
    for linha in linhas:
        for letra in linha:
            if letra ==caractere:
                cont +=1
print(cont)
