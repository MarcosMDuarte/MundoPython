d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

pd = d*60
pkm = km*0.15
t = pd+pkm

print('O total a pagar é de R${:.2f}.'.format(t))


#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de
#dias pelos quais ele foi alugado. Calcule o preço a pagar, sabemos que o carro custa R$60 e R$0,15 por Km rodado.