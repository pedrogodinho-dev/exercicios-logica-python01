n = int(input('Digite um numero inteiro: '))
if n > 0:
    if n % 2 == 0:
        print(f'O numero:{n} é POSITIVO e PAR')
    else:
        print(f'O numero:{n} é POSITIVO e IMPAR')
else:
    if n == 0:
        print('O numero é neutro (0)')
    else:
        if n % 2 ==0:
            print(f'O numero:{n} é NEGATIVO e PAR')
        else:
            print(f'O numero:{n} é NEGATIVO e IMPAR')
