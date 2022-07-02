'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

valor = float(input('Digite o valor do produto: R$'))
pag = int(input('Digite:\n1 para pagamento à vista em dinhero ou cheque.\n'
                             '2 para pagamento à vista no cartão.\n'
                             '3 para pagamento em 2x no cartão\n'
                             '4 para pagamento em 3x ou mais no cartão.\n'
                             'Qual sua escolha? '))

if pag == 1:
    print('Você obteve 10% de desconto. O valor a ser pago será de RS{:.2f}.'.format(valor-valor*0.10))
elif pag == 2:
     print('Você obteve 05% de desconto. O valor a ser pago será de RS{:.2f}.'.format(valor-valor*0.05))
elif pag == 3:
     print('Você pagará 10% de juros. O valor a ser pago será: RS{:.2f}.'.format(valor+valor*0.10))
elif pag == 4:
    parcela = int(input('Quantas parcelas?'))
    print('Sua compra será de {}X de {}'.format(parcela, (valor+valor*0.20)/parcela))
    print('Você pagará 20% de juros. O valor a ser pago será: RS{:.2f}.'.format(valor+valor*0.20))
else:
    print('Você não digitou uma opção válida. Comece o processo novamente.')