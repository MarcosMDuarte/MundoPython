# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a nome "SANTO"
cid = str(input('Digite o nome de uma cidade.')).strip()
print(cid[:5].upper() == 'SANTO')
