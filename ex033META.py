print('='*40)
print('1. X-Burger + Refrigerante: R$ 18,00 ')
print('2. X-Salada + Suco: R$ 22,00')
print('3. Hot Dog + Refrigerante: R$ 15,00')
print('4. Combo Família: R$ 50,00')
print('='*40)

opcao = (input('Qual opçao deseja escolher: '))
qtd = int(input('Quantos deseja: '))
valor = 0
match opcao:
    case '1':
        valor = 18.00 * qtd
    case '2':
        valor = 22.00 * qtd
    case '3':
        valor = 15.00 * qtd
    case '4':
        valor = 50.00 * qtd
    case _ :
        print('Opção invalida!')
if valor > 0:
    print(f'Você escolheu a opção {opcao} e o valor total é {valor:.2f}')
