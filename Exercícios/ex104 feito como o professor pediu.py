def leiaInt(a):
    while True:
        num = str(input(a))
        if num.isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\33[m')

    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de difitear o número {n}.')