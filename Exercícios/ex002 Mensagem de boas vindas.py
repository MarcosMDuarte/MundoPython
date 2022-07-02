nome = input("Qual seu nome? ")
sexo = str(input('Qual o seu sexo? [M/H]'))
if sexo in 'M':
    print("Seja muito bem vinda {}!".format(nome))
else:
    print("Seja muito bem vindo {}!".format(nome))
