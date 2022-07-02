'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos para pagamento? '))
meses = anos*12
pagamento = valor/meses
limite = sal*0.30
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}.'.format(valor, anos, pagamento))

if pagamento <= limite:
    print('Empréstimo APROVADO!')
else:
    print('Empréstimo NEGADO!')

