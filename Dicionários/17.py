#Faça um programa que controla o consumo de energia dos eletrodomésticos de uma casa e:
#Crie e leia 5 eletrodomésticos que contêm nome (máximo 15 letras), potência (real, em kW) e tempo ativo por dia (real, em horas).
#Leia um tempo t (em dias), calcule e mostre o consumo total (em kWh) na casa e o consumo relativo de cada eletrodoméstico (consumo/consumo total) nesse período de tempo. Apresente este último dado em porcentagem
energia = list()
for i in range(5):
    electro= dict()
    electro['nome'] = str(input())
    electro['potencia'] =float(input())
    electro['tempo'] = float(input())
    energia.append(electro)
t= int(input())
tot = 0
for electro in energia:
    consumo=electro['potencia']*electro['tempo']*t
    electro['consumo']=consumo
    tot+=consumo
print(f'{tot:.2f}')
for electro in energia:
    porcentual =(electro['consumo']/tot)*100
    print(f'{electro["nome"]}: {porcentual:.2f}')








