#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque
# esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadores = { 'jogador_1': randint(1, 6),
              'jogador_2': randint(1, 6),
              'jogador_3': randint(1, 6),
              'jogador_4': randint(1, 6)}
ranking = []

for k, v in jogadores.items():
    print(f'{k} tirou {v}. ')
    sleep(1)

print('-='*30)
print('== Raking ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, c in enumerate(ranking):
    print(f' {i+1}º lugar ficou o {c[0]} com {c[1]}')
    sleep(1)

