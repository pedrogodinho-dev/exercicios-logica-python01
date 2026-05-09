nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

pesoA = 3
pesoB = 3
pesoC = 4

if nota1 > 0 and nota2 > 0 and nota3 > 0:
    print('\nDigite 1 para média aritmética')
    print('Digite 2 para média ponderada com pesos 3, 3 e 4')
    print('Digite 3 para média harmônica')
    metodo = input('Digite qual média deseja apresentar: ')
    match metodo:
        case '1':
            media = (nota1 + nota2 + nota3) / 3
            print(f'O resultado da media aritmética é: {media:.2f}')
        case '2':
            media = (nota1 * pesoA + nota2 * pesoB + nota3 * pesoC) / (pesoA + pesoB + pesoC)
            print(f'O resultado da media ponderada é: {media:.2f}')
        case '3':
            media = 3 / (1/nota1 + 1/nota2 + 1/nota3)
            print(f'O resultado da media harmônica é: {media:.2f}')
        case _:
            print('ERRO: opção de menu invalida.')
else:
    print('ERRO: Digite apenas notas maiores que zero!')