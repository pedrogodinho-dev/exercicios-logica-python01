qtd = int(input('Qual a quantidade de maças? '))
if qtd > 12:
    valor = 1.0
    total = qtd * valor
else:
    valor = 1.30
    total = qtd * valor
print(f'Comprando {qtd} maçãs o valor é R${total:.2f}')