'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N]')).upper().strip()
    if res in 'Nn':
        break
    elif res not in 'SN':
        print('Resposta incorreta...')
        res = str(input('Quer continuar? [S/N]')).upper().strip()

for pos, n in enumerate(lista):
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')

