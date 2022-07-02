# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a
# criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# O número em cada jogo não pode repetir.
from random import randint
from time import sleep
cont = 0
jogos = []
temp = []
print('-'*40)
print(f'           JOGA NA MEGA SENA              ')
print('-'*40)

num = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, f'SORTEANDO {num} JOGOS', '=-'*5)
c = 1
while c <= num:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in temp:
            temp.append(n)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    c += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*4, '< BOA SORTE >', '-='*4)