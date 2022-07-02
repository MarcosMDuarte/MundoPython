#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas
#o nome com todas as letras minúsculas
#Quantas letras ao todo sem considerar espaços
#quantidade letras tem o primeiro nome



n = str(input('Digite seu nome completo:')).strip()
NOME = n.upper()
nome = n.lower()
ndividido = n.split()
contagemdeletras = len(ndividido[0])
contagem = len(n.strip()[0])
n = n.replace(" ", "")
contaletrassemespaco = len(n)
# n = len(n) - n.conut(' '). Assim ele vê o tamanho da string e retira o número de espaços.

print('Seu nome com todas as letras maiúsculas é: {}. \nCom letras minúsculas é: {}.\nAo todo possui {} letras e o primeiro nome possui {} letras.'.format(NOME, nome, contaletrassemespaco, contagemdeletras))
