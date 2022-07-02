'''Exercício Python 052: Faça um programa que leia um número inteiro e
diga se ele é ou não um número primo.'''

n = int(input('Digite um número:'))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[34m', end=' ')
        cont = cont + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

print('\033[m \n o número {} foi divisível {} vezes'.format(n, cont),end=' ')
if cont == 2:
    print('e por isso \033[34mÉ PRIMO'. format(n))
else:
    print('e por isso \033[31mNÃO É PRIMO!'. format(n))