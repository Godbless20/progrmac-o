#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais.
nome_arquivo = str(input())
with open(nome_arquivo,'r')as arquivo:
    linhas=arquivo.readlines()
    vogais='aeiouAEIOU'
    contador=0
    for linha in linhas:
        for caractere in linha:
            for v in vogais:
                if v == caractere:
                    contador +=1
                    break
print(contador)





