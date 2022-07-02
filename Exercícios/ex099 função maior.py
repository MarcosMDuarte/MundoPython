#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

from time import sleep
def maior (*num):
    num_maior = cont = 0
    print('-='*30)
    print('Analisando os valores passados...')

    for i in num:
        print(i, end= ' ')
        sleep(0.3)
        if cont == 0:
            num_maior = i
        else:
            num_maior = i
        cont +=1
    print(f'Forma informados {len(num)} valores ao todo.')
    print(f'O maior número informado foi {num_maior}')


#programa
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()