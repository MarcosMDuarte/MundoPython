'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
while True:
    numero_novo = int(input('Digite um valor: '))
    if numero_novo not in lista:
        lista.append(numero_novo)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()
    if cont == 'N':
        break

print(f'Você digitou os valores {sorted(lista)}')

