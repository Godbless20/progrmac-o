#Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada linha o nome de uma cidade e o seu número de habitantes, separados por uma tabulação. O programa deverá ler o arquivo de entrada, armazenar os dados das cidades em uma lista de dicionários, e gerar um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu número de habitantes. Mostre na tela lista dos dicionários e o conteúdo desse arquivo de saída.
def funcao(entrada,saida):
    cidades=list()
    with open(entrada,'r') as arquivo1:
        for linha in arquivo1:
            partes = linha.strip().split('\t')
            if len(partes)>=2:
                nome =partes[0]
                habitantes =int(partes[1])
                cidade = {
                    'nome': nome,
                    'habitantes': habitantes
                }
                cidades.append(cidade)


    mais_pop=0
    nome_mais_pop=''
    for cidade in cidades:
        if cidade['habitantes'] >mais_pop:
            mais_pop = cidade['habitantes']
            nome_mais_pop = cidade['nome']
        print(cidade)

    with open(saida,'w') as arquivo2:
        arquivo2.write(f'{nome_mais_pop}\t{mais_pop}')
    with open(saida,'r') as arquivo2:
        print(arquivo2.read())
entrada = str(input())
saida = str(input())
funcao(entrada,saida)


