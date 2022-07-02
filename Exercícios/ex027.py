#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#ex Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = str(input('Digite um nome complero: ')).strip()
divnome = nome.split()
prinome = divnome[0]
tamanho = len(divnome)-1
ultnome = divnome[len(divnome)-1]

print('O nome digitado foi: {}\nO primeiro nome é: {}.\nO último nome é: {}.'.format(nome,prinome,ultnome))
