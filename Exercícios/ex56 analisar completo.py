'''Exercício Python 56: Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
 qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''


sexo = ('Masculino', 'Feminino')
media = 0
hmv = ''
cont = 0
idadevelho = 0
for c in range(1, 5):
    nome = str(input('Qual seu nome? '))
    idade = int(input('Quantos anos você tem?'))
    media = media + idade
    print('Digite [ 1 ] para Homem e [ 2 ] para Mulheres.', end='')
    s = int(input('Qual seu sexo? '))
    if s == 1 and idade > idadevelho:
            hmv = nome
            idadevelho = idade
    elif idade < 20:
            cont += 1




print('A média de idade do grupo é {}'.format(media/c))
print('O homem mais velhor se chama {}'.format(hmv))
print('Número de mulheres mais novas de 20 anos é {}'.format(cont))