#Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’. Esse arquivo de saída deve ter o mesmo nome do arquivo de entrada, mas terminando em .out (por exemplo, se a entrada for arquivo.txt, a saída deve ser arquivo.txt.out). Escreva na tela o conteúdo desse arquivo.
nome_arquivo = str(input())
novo_caminho = nome_arquivo+'.out'
vogais= "aeiouAEIOU"
with open (nome_arquivo,'r') as arquivo:
    conteudo = arquivo.read()

novo_conteudo =''
for caractere in conteudo:
    vogal = False
    for v in vogais:
        if v ==caractere:
            vogal =True
            break
    if vogal:
        novo_conteudo +='*'
    else:
        novo_conteudo +=caractere
with open(novo_caminho,'w') as arquivo:
    arquivo.write(novo_conteudo)
print(novo_conteudo)
