'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
e = 0
while e != 5:
    print('-=='*12, '''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    e = int(input('>>>>>Escolha a opção desejada: '))
    if e == 1:
        r = n1 + n2
        print('O resultado da soma entre {} e {} é {}.'.format(n1, n2, r))
    elif e == 2:
        r = n1 * n2
        print('O resultado da multiplicação entre {} e {} é {}.'.format(n1, n2, r))
    elif e == 3:
        if n1 > n2:
            nm = n1
        else:
            nm = n2
        print('O número maio é {}'.format(nm))
    elif e == 4:
        print('Insira dos números novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif e == 5:
        print('Você escolheu sair do programa...')
        sleep(1)
    else:
        print('Você digitou a opção errada. Comece novamente.')



print('FIM')