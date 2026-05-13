ano_atual = 2026
ano1 = int(input('Digite o ano de nascimento: '))
ano2 = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano1
idade2 = ano_atual - ano2

if idade > idade2:
    print(f'O mais novo é: {idade2}')
else:
    if ano1 == ano2:
        print('Tem a mesma idade aproximada')
    else:
        print(f'O mais novo é: {idade}')