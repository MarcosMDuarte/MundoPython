#pergunte a distância de uma viagem em KM, calcule o preço da passagem, cobrando 050 por km até 200 e 0.45 para mis longas

km = float(input('Qual a distância em km que pretende viajar? '))
if km <= 200:
    print('O valor da sua passagem é R${}'.format(km*0.5))
else:
    print('O valor da passagem é R${}'.format(km*0.45))