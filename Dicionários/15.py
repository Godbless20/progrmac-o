#Faça um programa que leia um vetor com dados de 5 livros: título, autor e ano. Procure um livro por título, perguntando ao usuário qual título deseja buscar. Mostre os dados de todos os livros encontrados. O título procurado não precisa ser exato, ou seja, os livros encontrados devem ser aqueles que contêm o título buscado.
vetor = []


for i in range(5):
    livro = {}
    titulo = input()
    autor = input()
    ano = int(input())
    livro['titulo'] = titulo
    livro['autor'] = autor
    livro['ano'] = ano
    vetor.append(livro)


busca = input()
busca2 = ""
for i in range(len(busca)):
    c = busca[i]
    if c != ' ':
        if 'A' <= c <= 'Z':
            busca2 += chr(ord(c) + 32)
        else:
            busca2 += c


for i in range(5):
    titulo = vetor[i]['titulo']
    t2 = ""
    for j in range(len(titulo)):
        c = titulo[j]
        if c != ' ':
            if 'A' <= c <= 'Z':
                t2 += chr(ord(c) + 32)
            else:
                t2 += c

    achou = False
    for j in range(len(t2) - len(busca2) + 1):
        igual = True
        for k in range(len(busca2)):
            if t2[j + k] != busca2[k]:
                igual = False
        if igual:
            achou = True

    if achou:
        print(vetor[i])
