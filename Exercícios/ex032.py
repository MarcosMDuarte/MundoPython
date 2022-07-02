#Faça um programa que leia um ano qualquer e mosrtre se ele é BISSEXTO
from datetime import date

ano = int(input('Qual ano quer analisar? Digite "0" para o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))