'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. '''

from random import randint
vitorias = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-'*20)
while True:
    comp = randint(1, 20)
    n = int(input('Diga um valor: '))
    r = str(input('Par ou Ímpar?' )).strip().upper()[0]
    print('-'*30)
    soma = n + comp
    res = soma % 2
    if r == 'P':
        if res == 0:
            print(f'Você jogou {n} e o computador {comp}. Total de {soma} DEU PAR')
            print('Você VENCEU !')
            vitorias +=1
            print('Vamos jogar novamente...')
            print('=-'*15)
        else:
            print(f'Você jogou {n} e o computador {comp}. Total de {soma} DEU ÍMPAR')
            break
    else:
        if res != 0:
            print(f'Você jogou {n} e o computador {comp}. Total de {soma} DEU ÍMPAR')
            print('Você VENCEU !')
            vitorias += 1
            print('Vamos jogar novamente...')
            print('=-' * 15)
        else:
            print(f'Você jogou {n} e o computador {comp}. Total de {soma} DEU PAR')
            break
print('Você PERDEU !')
print('=-'*20)
print(f'GAMER OVER! Você venceu {vitorias} vezes.')