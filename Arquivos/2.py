#Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas esse arquivo possui
nome_arquivo =str(input())
with open(nome_arquivo,'r') as arquivo:
    linha = arquivo.readlines()
    print(len(linha))
