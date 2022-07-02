#Escreva um programam  que leia a velocidade de um
#(carro)se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7,00 por cada km acima do limite

vel = float(input('Digite a velocidade do seu carro em km: '))

if vel > 80:
    print('Você foi multado!! O valor a ser pago é de R${:.2f}'.format((vel-80)*7))
print('Tenha um bom dia!')