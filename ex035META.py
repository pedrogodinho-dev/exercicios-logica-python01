print('=' *40)
print('Código 100: Cachorro-quente — R$ 12,00')
print('Código 101: Bauru simples — R$ 15,00')
print('Código 102: Hambúrguer — R$ 20,00')
print('Código 103: Cheeseburguer — R$ 22,00')
print('Código 104: Refrigerante — R$ 7,00')
print('='*40)

valor = int(input('Digite o codigo: '))
match valor:
    case 100:
        preco = 12.00
    case 101:
        preco = 15.00
    case 102:
        preco = 20.00
    case 103:
        preco = 22.00
    case 104:
        preco = 7.00
    case _ :
        preco = 0

if preco == 0:
    print('Codigo invalido!')
else:
    qtd = int(input('Qual a quantidade deseja comprar ?'))
    total = preco * qtd
    print(f'Valor total é R$ {total:.2f}')
