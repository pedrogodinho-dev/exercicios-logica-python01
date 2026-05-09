num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
num3 = int(input('Digite outro numero: '))

if num1 > num2 and num1 > num3:
    print(f'O numero maior é {num1}')
else:
    if num2 > num3:
        print(f'O numero maior é {num2}')
    else:
        print(f'O numero maior é {num3}')
