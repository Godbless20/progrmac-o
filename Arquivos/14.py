#Dado um arquivo contendo um conjunto de nomes e datas de nascimento (DD MM AAAA, isto é, 3 inteiros em sequência), faça um programa que leia o nome do arquivo e a data de hoje e construa outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo. No arquivo de entrada, o nome está separado da data de nascimento por uma tabulação, mas as informações da data de nascimento estão separadas por um espaço em branco. A data de hoje da entrada será dada em três inteiros diferentes, dia, mês e ano. O arquivo de saída deve ter o mesmo nome do arquivo de entrada, mas terminando em .out (por exemplo, se a entrada for arquivo.txt, a saída deve ser arquivo.txt.out). Escreva na tela o conteúdo desse arquivo.
def eh_idade(dn, mn, an, dh, mh, ah):
    idade = ah - an
    if mh < mn:
        idade = idade - 1
    elif mh == mn:
        if dh < dn:
            idade = idade - 1
    return idade

def processar(nome_arquivo, dia_hoje, mes_hoje, ano_hoje):
    nome_saida = nome_arquivo + '.out'
    linhas_saida = []

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        linha = linha.strip()

        pos_tab = -1
        for j in range(len(linha)):
            if linha[j] == '\t':
                pos_tab = j
                break

        if pos_tab != -1:
            nome = linha[:pos_tab]
            data = linha[pos_tab + 1:]

            partes = []
            atual = ''
            for c in data:
                if c == ' ':
                    partes.append(atual)
                    atual = ''
                else:
                    atual = atual + c
            partes.append(atual)

            dia_nasc = int(partes[0])
            mes_nasc = int(partes[1])
            ano_nasc = int(partes[2])

            idade = eh_idade(dia_nasc, mes_nasc, ano_nasc, dia_hoje, mes_hoje, ano_hoje)
            linha_saida = nome + '\\t' + str(idade)
            linhas_saida.append(linha_saida)

    with open(nome_saida, 'w') as saida:
        for linha in linhas_saida:
            saida.write(linha + '\n')

    with open(nome_saida, 'r') as exibir:
        linhas_novas = exibir.readlines()
        for linha in linhas_novas:
            print(linha.strip())
arquivo = input()
dia = int(input())
mes = int(input())
ano = int(input())

processar(arquivo, dia, mes, ano)

