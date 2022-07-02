'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import choice

lista = ['pedra', 'papel', 'tesoura']
maquina = choice(lista)
jogador = str(input('Você quer pedra, papel ou tesoura? ')).strip().lower()

if jogador == maquina:
    print('Empate')
elif jogador == 'pedra' and maquina == 'tesoura' or jogador == 'tesoura' and maquina == 'papel' or jogador == 'papel' and maquina == 'pedra':
    print('Você ganhou!')
else :
    print('Você perdeu!')

print('Você escolheu {} e a maquina escolheu {}.'.format(jogador,maquina))