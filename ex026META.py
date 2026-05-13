a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print(f'O numero {a} é maior que o numero {b}')
else:
    if a == b:
        print(f'Os numeros são iguais')
    else:
        print(f'O numero {b} é maior que o numero {a}')