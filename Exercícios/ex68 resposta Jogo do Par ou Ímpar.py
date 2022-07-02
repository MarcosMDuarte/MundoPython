'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. '''

from random import randint
vitorias = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-'*20)
while True:
    comp = randint(0, 10)
    n = int(input('Diga um valor: '))
    soma = n + comp
    res = soma % 2
    tipo =' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {n} e o computador {comp}. Total de {soma}', end=' ')
    print('DEU PAR' if res == 0 else 'DEU IMPAR')
    print('-'*30)
    if tipo == 'P':
        if res == 0:
            print('Você VENCEU !')
            vitorias +=1
        else:
            break
    else:
        if res != 0:
            print('Você VENCEU !')
            vitorias += 1
        else:
            break
    print('Vamos jogar novamente...')
print('Você PERDEU !')
print('=-'*20)
print(f'GAMER OVER! Você venceu {vitorias} vezes.')