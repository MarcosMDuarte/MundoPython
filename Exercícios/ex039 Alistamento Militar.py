'''
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
 ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date
sexo = str(input('Qual seu sexo?'))
mulher = 'mulher'
homem = 'homem'
nas = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nas
print('Quem nasceu em {} tem {} anos em {}'.format(nas, idade, date.today().year))
print('Seu sexo é {}'.format(sexo))
if sexo == mulher:
    print('Você não precisa se alistar')
elif idade == 18:
    print('Hora exata para se alistar')
elif idade > 18:
    print('Já passou da hora de se alistar')
elif idade == 17:
    print('Ainda falta 1 ano para você se alistar')
else:
    print('Ainda faltam {} ano para você se alistar'.format(18-idade))

