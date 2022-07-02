'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
 alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''


print('='*30)
print('   10 TERMOS DE UMA PA')
print('='*30)

n = n1 = int(input('Primeiro termo: '))
r = r1 = int(input('Razão: '))
t = 0
mais = 10
c = 1
while mais != 0:
    t += mais
    while c <= t:
        print(n, end=' -> ')
        n = n + r
        c +=1
    print('pausa...')
    mais = int(input('Quantos termos você quer a mais? '))
print('A progressão foi finalizada mostrando {} termos, partindo de {}, com razão {} e totalizando {}!'.format(t, n1, r1, n-r1))