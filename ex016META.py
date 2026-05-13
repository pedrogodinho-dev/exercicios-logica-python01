lado_a = int(input('Digite o valor de A: '))
lado_b = int(input('Digite o valor de B: '))
lado_c = int(input('Digite o valor de C: '))
s = 0
if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    p = (lado_a+lado_b+lado_c) / 2
    area = (p * (p - lado_a) * (p - lado_b) * (p - lado_c)) ** 0.5
    print('É um triangulo')
    print(f'Sua area é: {area:.2f}')
else:
    print('Não é um triangulo')