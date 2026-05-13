a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))

print('Digite a forma que quer que os numeros sejam exibidos')
print('Digite 1 para mostrar os valores em ordem crescentes')
print('Digite 2 para mostrar os valores em ordem decrescentes')
print('Digite 3 para que o maior numero fique no meio')

forma = input('Digite ama opção: ')
match forma:
    case '1':
        if a > b and a > c:
            if b > c:
                print(f'Em ordem crescente: {a},{b} e {c}')
            else:
                print(f'Em ordem crescente: {a},{c} e {b}')
        else:
            if b > a and b > c:
                if a > c:
                    print(f'Em ordem crescente: {b},{a} e {c}')
                else:
                    print(f'Em ordem crescente: {b},{c} e {a}')
            else:
                if a > b:
                    print(f'Em ordem crescente: {c},{a} e {b}')
                else:
                    print(f'Em ordem crescente: {c},{b} e {a}')
    case '2':
        if a < b and a < c:
            if b < c:
                print(f'Em ordem crescente: {a},{b} e {c}')
            else:
                print(f'Em ordem crescente: {a},{c} e {b}')
        else:
            if b < a and b < c:
                if a < c:
                    print(f'Em ordem crescente: {b},{a} e {c}')
                else:
                    print(f'Em ordem crescente: {b},{c} e {a}')
            else:
                if a < b:
                    print(f'Em ordem crescente: {c},{a} e {b}')
                else:
                    print(f'Em ordem crescente: {c},{b} e {a}')
    case '3':
        if a > b and a > c:
            print(f'O maior no meio: {b}, {a} e {c}')
        else:
            if b > a and b > c:
                print(f'O maior no meio: {a}, {b} e {c}')
            else:
                print(f'O maior no meio: {b}, {c} e {a}')
    case _:
        print('Opção invalida!')