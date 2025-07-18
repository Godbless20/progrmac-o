#Continuando o programa da questão anterior, escreva no arquivo de saída, além da idade, uma string que representa a sua maioridade:
#◦ Se a idade for menor do que 18 anos, escreva “menor de idade”
#◦ Se a idade for maior do que 18 anos, escreva “maior de idade”
#◦ Se a idade for igual a 18 anos, escreva “entrando na maioridade”
def eh_idade(dn, mn, an, dh, mh, ah):
    idade = ah - an
    if mh < mn:
        idade = idade - 1
    elif mh == mn:
        if dh < dn:
            idade = idade - 1
    return idade

def classificacao_maioridade(idade):
    if idade < 18:
        return 'menor de idade'
    elif idade > 18:
        return 'maior de idade'
    else:
        return 'entrando na maioridade'

def processar(nome_arquivo, dia_hoje, mes_hoje, ano_hoje):
    nome_saida = nome_arquivo + '.out'
    linhas_saida = []

    with open(nome_arquivo) as arquivo:
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

            dn = int(partes[0])
            mn = int(partes[1])
            an = int(partes[2])

            idade = eh_idade(dn, mn, an, dia_hoje, mes_hoje, ano_hoje)
            tipo = classificacao_maioridade(idade)
            linha_saida = nome + '\\t' + str(idade) + '\\t' + tipo
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

