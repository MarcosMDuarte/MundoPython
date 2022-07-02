#Crie um prgrama que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

n = input('Digite seu nome completo:').strip()
ver = 'SILVA' in n.upper()
print('Você é da família Silva? {}'.format(ver))
