h1 = int(input('Digite a idade do primeiro homem: '))
h2 = int(input('Digite a idade do segundo homem: '))
m1 = int(input('Digite a idade da primeira mulher: '))
m2 = int(input('Digite a idade da segunda mulher: '))
if h1 > h2 and m1 < m2:
    soma = h1 + m1
    multiplicacao = h2 * m2
else:
    if h2 > h1 and m2 < m1:
        soma = h2 + m2
        multiplicacao = h1 * m2
print(f'A soma do homem mais velho com a mulher mais nova é = {soma}')
print(f'A multiplicação do homem mais novo com a mulher mais velha é = {multiplicacao}')