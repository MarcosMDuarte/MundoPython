#Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três
# contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep
def contagem (i, f, p):
    print('-='*30)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end= ' ')
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
    print()


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-='*30)
print('Agora é dua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
