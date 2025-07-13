#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.
nome_arquivo = str(input())
with open(nome_arquivo,'r')as arquivo:
    linhas=arquivo.readlines()
    vogais='aeiouAEIOU'
    consoantes='bcdfghjklmnpqrstvwxyBCDFGHJKLMNPQRSTVWXY'
    cont_vog=0
    cont_con =0
    for linha in linhas:
        for caractere in linha:
            for v in vogais:
                if v == caractere:
                    cont_vog +=1
                    break


            for con in consoantes:
                if caractere == con:
                    cont_con +=1
                    break
print(cont_vog)
print(cont_con)





