# Faqça um programa que leia um ângulo qualuqer e mostra na tela o valor do seno, cosseno e tangente desse ângulo
# achar o módulo certo para isso
from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo para desconbrir o seno, cosesno e tangente: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print('Com o ângulo {}º: \n O Seno é {:.2f}; \n O Consseno é {:.2f}; \n A tangente é {:.2f}.'.format(ang, sen, cos, tan))