#Faça um programa que leia uma frase pelo teclado e mostre:

#Quantas vezes aparece a letra  "A".

#Em que posição ela parece a primeira
#Em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).upper().strip()
conta = frase.count('A')
pripos = frase.find('A')+1
ultpos = frase.rfind('A')+1

print('A letra "A" aparece {} vezes.\nNa primeira vez está na posição {}\nNa última vez está na posição {}'.format(conta,pripos,ultpos))
