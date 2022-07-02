""" Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto."""

'''sexo = 'A'
while sexo == 'A':
    sexo = str(input('Qual seu sexo? [M/F]')).upper()
    if sexo == 'M':
        print('Você é um homem.')
    elif sexo == 'F':
        print('Você é mulher.')
    else:
        print("Você digitou a resposta errada utilize as letras 'M' ou 'F'")
        sexo = 'A'
print('FIM')'''

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]