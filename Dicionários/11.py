#Faça um programa que faça operações simples de números complexos:
#◦ Crie e leia dois números complexos z e w, compostos por parte real e parte imaginária.
#◦ Apresente a soma, subtração e produto entre z e w, nessa ordem, bem como o módulo de ambos. Cada operação deve ser feita em uma função diferente.
from math import sqrt
def eh_soma(z,w):
    return {'real':z['real']+w['real'], 'imaginario':z['imaginario'] + w['imaginario']}
def eh_subtracao(z,w):
    return {'real': z['real'] - w['real'], 'imaginario':z['imaginario']- w['imaginario']}
def eh_produto(z,w):
    real = z['real']*w['real'] -z['imaginario']*w['imaginario']
    imag = z['real'] * w['imaginario'] + z['imaginario'] * w['real']
    return {'real': real, 'imaginario': imag}
def eh_modulo(c):
    return f"{sqrt(c['real']**2 + c['imaginario']**2):.2f}"

real_z = float(input())
imag_z = float(input())
z = {'real': real_z, 'imaginario': imag_z}
real_w = float(input())
imag_w = float(input())
w = {'real': real_w, 'imaginario': imag_w}
print(eh_soma(z, w))
print(eh_subtracao(z, w))
print(eh_produto(z, w))
print(eh_modulo(z))
print(eh_modulo(w))
