def escreva (msg):
    print('~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))

while True:
    mensagem = str(input('Escreva seu título: '))
    escreva(mensagem)
    while True:
        res = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if res in 'SN':
            break
        else:
            print('ERRO! Responda S ou N')
    if res in 'N':
        break