'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(0, 7):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(c+1)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade \nE também tivemos {} menores de idade'.format(maior, menor))

