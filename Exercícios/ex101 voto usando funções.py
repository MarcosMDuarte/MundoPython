#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.


def voto(nascimento):
    from datetime import date
    idade = date.today().year - ano
    print(f'Você tem {idade} anos. Então seu voto é', end=' ')
    if idade < 16:
        print('negado')
    elif idade < 18 or idade > 65:
        print('opcional')
    else:
        print('obrigatório')

print('-='*30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)