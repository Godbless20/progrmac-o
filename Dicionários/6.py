#Considerando o dicionário com chaves “x”, “y” e “z” para representar um vetor tridimensional, implemente uma função que calcule a soma de dois vetores, e um programa que peça valores para o usuário, use essa função, e mostre o resultado
def funcao(vet1,vet2):
    return{
        "x":vet1[0]+vet2[0],
        "y":vet1[1]+vet2[1],
        "z":vet1[2]+vet2[2]
    }
vetor1=list()
vetor2=list()
for i in range(3):
    vetor1.append(float(input()))
for j in range(3):
    vetor2.append(float(input()))
print(funcao(vetor1,vetor2))

