#Faça um programa que leia um vetor com os dados de 5 carros: marca, ano e preço. Leia um valor p e mostre as informações de todos os carros com preço menor que p. Repita este processo até que seja lido um valor p = 0.
vetor=list()
for i in range(5):
    carro=dict()
    carro['modelo'] = str(input())
    carro['ano'] = int(input())
    carro['preco'] =float(input())
    vetor.append(carro)
while True:
    p = int(input())
    for carro in vetor:
       if carro['preco']< p :
           print(carro)
    if p == 0:
        break

