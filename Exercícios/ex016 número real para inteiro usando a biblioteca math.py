# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#ex. 6.127 tem a porte inteira 6.
from math import trunc
num = float(input("Digite um número real:"))
print('O valor digitado doi {} e sua porção inteira é {}.'.format(num, trunc(num)))

