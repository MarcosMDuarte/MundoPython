'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
lista_temporarea = []
lista_principal = list()
mai = men = 0
while True:
    lista_temporarea.append(str(input('Nome: ')))
    lista_temporarea.append(int(input('Peso: ')))
    # para identificar quem tem o peso maior
    if len(lista_principal) == 0:
        men = mai = lista_temporarea[1]
    else:
        if lista_temporarea[1] >= mai:
            mai = lista_temporarea[1]
        if lista_temporarea[1] <= men:
            men = lista_temporarea[1]

    lista_principal.append(lista_temporarea[:])
    lista_temporarea.clear()
    res = str(input('Quer continuar? [S/N]')).upper().strip()
    if res in 'N':
        break

print(f'Foram cadastradas {len(lista_principal)} pessoas.')
print(f'A pessoa mais pesada tem {mai}Kg e seus nomes são: ', end= '')
for p in lista_principal:
    if p[1] == mai:
        print(f'[{p[0].upper()}]',end='')
print(f'\nA pessoa mais leve tem {men}Kg e seus nomes são: ', end='')
for p in lista_principal:
    if p[1] == men:
        print(f'[{p[0].upper()}]', end='')