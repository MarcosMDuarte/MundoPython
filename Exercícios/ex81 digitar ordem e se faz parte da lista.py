'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, mostre:
 A) Quantos números foram digitados.
 B) A lista de valores, ordenada de forma decrescente.
 C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N]')).upper().strip()
    if res in 'Nn':
        break
    elif res not in 'SN':
        print('Resposta incorreta...')
        res = str(input('Quer continuar? [S/N]')).upper().strip()
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores na ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
