# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO DE 0 A 5 E PRÇA PARA
# O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR

from random import randint
from time import sleep
print('-=-'*20)
print('   Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = int(randint(0,5))
ten = int(input("Em que número eu pensei? "))

print('Processando...')
sleep(3)
if ten == num:
    print('Parabéns, você acertou!!')
else:
    print('Você errou! Não foi dessa vez. O número que eu pensei foi {}.'.format(num))
