a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a == 0 or b == 0:
    print('Operação não permitida!')
else:
    div = a / b
    print(f'Resultado {div}')