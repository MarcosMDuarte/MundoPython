'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

l1 = float(input('Digite a medida de uma reta: '))
l2 = float(input('Digite a medida de uma reta: '))
l3 = float(input('Digite a medida de uma reta: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Forma um triângulo e ele é', end='')
    if l1 == l2 and l1 == l3:
        print(' EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print(' ISÒCELES')
    else:
        print(' ESCALENO')
else:
    print('Não é um triângulo')