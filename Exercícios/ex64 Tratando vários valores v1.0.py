'''Exercício Python 064: Crie um programa que leia vários números inteiros pelo
teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles (desconsiderando o flag).

s = 0
c = 1
n = int(input('Digite um número: '))
controle = False
while not controle:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        c += 1
    else:
           controle = True
print('Você digitou {} números e sua soma totaliza {}'.format(c, s))'''

c = s = 0
n = int(input('Digite um número: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número: '))
print('Você digitou {} números e sua soma totaliza {}'.format(c, s))
