#Faça um programa que leia o conteúdo de um arquivo e crie outro arquivo com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário. Escreva na tela o conteúdo dos dois arquivos, primeiro o do arquivo de entrada e depois o do arquivo de saída.
nome_caminho1 =str(input())
nome_caminho2 = str(input())

with open (nome_caminho1,'r') as arquivo:
    conteudo = arquivo.read()

novo_conteudo =''
for caractere in conteudo:
    if 'a'<= caractere <='z':
        novo_conteudo +=chr(ord(caractere)-32)
    else:
        novo_conteudo+=caractere
with open(nome_caminho2,'w') as saida:
    saida.write(novo_conteudo)

print(conteudo,end='')
print(novo_conteudo)
