#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
# sorteados pela função anterior.

from random import randint
from time import sleep
a = int(input('Digite a quantidade de números sorteados: '))
def sorteador(a):
    cont = 0
    while cont < a:
        num = randint(0,10)
        list.append(num)
        print(f'{num}', end= ' ')
        sleep(0.5)
        cont +=1
    print()


def somaPar(l):
    soma = 0
    for i in l:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares em {l}, temos {soma}')

list = []
sorteador(a)
somaPar(list)
