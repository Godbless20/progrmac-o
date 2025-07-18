#Abra um arquivo texto, calcule e escreva na tela o número de caracteres, o número de linhas e o número de palavras neste arquivo. Também escreva na tela quantas vezes cada letra ocorre no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais caracteres espaço, tabulação ou nova linha.
def limpar_letra(letra):
    acentuados = 'áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ'
    sem_acentos = 'aaaaeeiooouucAAAAEEIOOOUUC'
    i = 0
    while i < len(acentuados):
        if letra == acentuados[i]:
            return sem_acentos[i].lower()
        i += 1
    return letra.lower()

def analisar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()

    num_caracteres = 0
    num_linhas = 0
    num_palavras = 0
    letras = {}
    palavra_em_andamento = False
    i = 0

    while i < len(texto):
        char = texto[i]
        num_caracteres += 1

        if char == '\n':
            num_linhas += 1

        if char == ' ' or char == '\n' or char == '\t':
            if palavra_em_andamento:
                num_palavras += 1
                palavra_em_andamento = False
        else:
            palavra_em_andamento = True

        eh_letra = False
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            eh_letra = True
        else:
            j = 0
            acentuados = 'áàâãéêíóôõúüçÁÀÂÃÉÊÍÓÔÕÚÜÇ'
            while j < len(acentuados):
                if char == acentuados[j]:
                    eh_letra = True
                    break
                j += 1

        if eh_letra:
            letra = limpar_letra(char)

            existe = False
            for chave in letras:
                if chave == letra:
                    existe = True
                    break

            if existe == False:
                letras[letra] = 1
            else:
                letras[letra] = letras[letra] + 1

        i += 1

    if palavra_em_andamento:
        num_palavras += 1

    print(num_caracteres)
    print(num_linhas)
    print(num_palavras)
    letra_atual = 'a'
    while letra_atual <= 'z':
        encontrada = False
        for chave in letras:
            if chave == letra_atual:
                encontrada = True
                break
        if encontrada:
            print(letra_atual + ":", letras[letra_atual])
        else:
            print(letra_atual + ":", 0)

        letra_atual = chr(ord(letra_atual) + 1)
arquivo = input()
analisar_arquivo(arquivo)