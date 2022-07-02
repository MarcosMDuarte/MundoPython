'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''
num = int(input('Digite um número para saber seu fatorial: '))
cont = num
f = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print('x' if cont > 1 else '= ', end='')
    f = f * cont
    cont -= 1
print(f)

