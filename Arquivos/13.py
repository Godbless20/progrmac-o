#Faça um programa que leia um arquivo com diversos nomes e telefones cadastrados, um por linha, e separados por uma tabulação. Guarde essas informações em uma lista de dicionários. Imprima esses dicionários na tela, ordenados pelo nome. O nome do arquivo é dado como entrada para o programa
def ler_informacoes(nome_arquivo):
    contatos = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        linha = linha.strip()

        pos_tab = -1
        for i in range(len(linha)):
            if linha[i] == '\t':
                pos_tab = i
                break

        if pos_tab != -1:
            nome = linha[:pos_tab]
            telefone = linha[pos_tab + 1:]
            contato = {'nome': nome, 'telefone': telefone}
            contatos.append(contato)

    for i in range(len(contatos)):
        for j in range(i + 1, len(contatos)):
            if contatos[j]['nome'] < contatos[i]['nome']:
                temp = contatos[i]
                contatos[i] = contatos[j]
                contatos[j] = temp

    for contato in contatos:
        print(contato)


arquivo = input()
ler_informacoes(arquivo)

