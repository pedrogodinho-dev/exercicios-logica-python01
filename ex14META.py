ABCD = 12.00
XYPK = 18.00
KLMP = 32.00
QRST = 40.00
codigo = input('Qual o codigo? ').upper().strip()
match codigo:
    case 'ABCD':
        valor = ABCD
    case 'XYPK':
        valor = XYPK
    case 'KLMP':
        valor = KLMP
    case 'QRST':
        valor = QRST
    case _:
        valor = -1
if valor == -1:
    print('Valor invalido')
else:
    qtd = int(input('Qual a quantidade? '))
    valor_total = valor*qtd
    print(f'Valor total: {valor_total}')