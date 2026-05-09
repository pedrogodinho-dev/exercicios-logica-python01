print("--- TABELA DE PRODUTOS ---")
print("cod1: R$10.00 | cod2: R$18.00 | cod3: R$23.00")
print("cod4: R$26.00 | cod5: R$32.00")
codigo = input('Digite o codigo do produto: ').lower().strip()
match codigo:
    case 'cod1':
        preco = 10.00
    case 'cod2':
        preco = 18.00
    case 'cod3':
        preco = 23.00
    case 'cod4':
        preco = 26.00
    case 'cod5':
        preco = 32.00
    case _:
        preco = -1
if preco == -1:
    print('Digite um codigo valido.')
else:
    qtd = int(input('Informe a quantidade de produtos: '))
    valor_total = preco*qtd
    print(f'O valor total da compra foi R${valor_total:.2f}')