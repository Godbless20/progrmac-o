carros=list()
maior =0
mais_consumo = ''
for i in range(5):
    modelo=dict()
    modelo['carro']=str(input(''))
    modelo['consumo']=float(input())
    carros.append(modelo.copy())
    if modelo['consumo'] >maior:
        maior= modelo['consumo']
        mais_consumo=modelo['carro']
print(f'Carro mais economico: {mais_consumo}')

for carro in carros:
    autonomia = carro['consumo']*50
    print(f'Carro {carro["carro"]} percorre {autonomia:.2f} kms com 50 litros')
for carro in carros:
    litros = 1000/carro["consumo"]
    print(f'Carro {carro["carro"]} precisa de {litros:.2f} litros para percorrer 1000 kms ')
