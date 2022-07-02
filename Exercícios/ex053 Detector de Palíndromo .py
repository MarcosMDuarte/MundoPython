'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''

frase = str(input('Digite uma frase: ')).strip().upper() #stip elimina espaços anteriores e upper deixa em maiúscula
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('o inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')