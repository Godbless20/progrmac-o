#Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo). O nome do terceiro arquivo deve ser o nome do primeiro arquivo seguido do nome do segundo arquivo. Mostre na tela o conteúdo do terceiro arquivo.
def eh_arquivo3(arquivo1,arquivo2):
    nome_terceiro = arquivo1+arquivo2
    with open(nome_terceiro,'w') as funcao3:
        funcao3.write(conteudo1+conteudo2)
    with open(nome_terceiro,'r') as funcao3:
        print(funcao3.read())
arquivo1=str(input())
arquivo2=str(input())
with open(arquivo1,'r') as funcao1:
    conteudo1=funcao1.read()
with open (arquivo2,'r') as funcao2:
    conteudo2 = funcao2.read()
eh_arquivo3(arquivo1,arquivo2)