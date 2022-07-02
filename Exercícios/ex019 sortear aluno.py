# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
#ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice,

a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome de outro aluno: ')
a3 = input('Digite o nome de outro aluno: ')
a4 = input('Digite o nome de outro aluno: ')

lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print('O escolhido foi {}'.format(escolhido))