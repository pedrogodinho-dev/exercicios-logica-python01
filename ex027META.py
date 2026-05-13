nome1 = (input('Primeiro nome: '))
nome2 = (input('Segundo nome: '))

peso1 = float(input(f'Digite o peso do {nome1}: '))
peso2 = float(input(f'Digite o peso do {nome2}: '))

if peso1 > peso2:
    print(f'O(a) {nome1} é mais pesado e pesa {peso1}')
else:
    if peso2 == peso1:
        print('O dois são o mesmo peso!')
    else:
        print(f'O(a) {nome2} é mais pesado e pesa {peso2}')