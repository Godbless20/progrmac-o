#Faça uma função que recebe o nome do arquivo e uma palavra, e retorne o número de vezes que aquela palavra aparece no arquivo.
def funcao(nome_arquivo, palavra):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read().lower()

    contador = 0
    for i in range(len(texto) - len(palavra) + 1):
        if texto[i:i + len(palavra)] == palavra.lower():
            contador += 1
    return contador