# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
ca = float(input('Digite um dos Catetos:'))
co = float(input('Digite o outro Cateto: '))
hi = hypot(ca,co)
print('A hipotenusa vai medir {:.2f}'.format(hi))