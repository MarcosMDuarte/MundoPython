'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep

'''print('-=-'*20)
print('   Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
num = int(randint(0,10))
ten = int(input('Em que número eu pensei? '))
cont = 1
sleep(1)
while num != ten:
    ten = int(input('Você errou, tente novamente: '))
    cont += 1
    sleep(1)

print('Parabéns! Você acertou! Você tentou {} vezes.'.format(cont))'''

print('-=-'*20)
print('   Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
computador = int(randint(0,10))
acertou = False
ten = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    ten += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        else:
            print('Menos... tente novamente.')
print('Acertou com {} tentativas. Parabéns!'.format(ten))



