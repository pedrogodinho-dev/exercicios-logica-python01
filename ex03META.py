num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > 0 and num2 > 0:
    if num1 > num2:
        print(f'O numero menor é {num2} e o maior é {num1}')
    else:
        print(f'O numero menor é {num1} e o maior é {num2}')
else:
    print('Você digitou um numero invalido!')