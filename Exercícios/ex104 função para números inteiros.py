def leiaInt():
    while True:
        num = str(input('Digite um número inteiro: '))
        if num.isnumeric():
            break
        else:
            print('ERRO! Digite um número inteiro válido')



leiaInt()