qtd_produtos = int(input("Quantos produtos você vendeu? "))

if qtd_produtos <= 250:
    valor = qtd_produtos * 1.00
    print('a')
else:
    if qtd_produtos <= 500:
        print('b')
        valor = qtd_produtos * 1.50
    else:
        print('c')
        valor = qtd_produtos * 2.00
print(f'Você vendeu {qtd_produtos} produtos e recebeu R${valor} de comissão! ')