#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('Digite o nome de um aluno: ')
a2 = input('Digite o nome de outro aluno: ')
a3 = input('Digite o nome de outro aluno: ')
a4 = input('Digite o nome de outro aluno: ')

lista = [a1, a2, a3, a4]
shuffle(lista)

print('A ordem de apresentação é: ')
print(lista)