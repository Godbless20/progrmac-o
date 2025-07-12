#Faça um programa que converta coordenadas polares para cartesianas:
#◦ Crie e leia um ponto em coordenada polar, composto por raio (r) e ângulo (a) em radianos.
#◦ Crie outro ponto, agora em coordenada cartesiana, composto por x e y, sabendo que x = r * cos(a) e y = r * sin(a).
#No programa principal, leia um ponto em coordenada polar, mostre esse ponto, e mostre as coordenadas do ponto convertido para o plano cartesiano. A conversão deve ser feita em uma função.
from math import sin,cos
def funcao(r,a):
   print({'r':r, 'a':a})
   print({'x':cos(a)*r, 'y':sin(a)*r})
raio = float(input())
angulo = float(input())
funcao(raio,angulo)
