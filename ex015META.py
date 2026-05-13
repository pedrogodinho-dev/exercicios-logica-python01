cargo = (input('Qual o codigo do seu cargo: '))
salario_atual = float(input('Qual o seu salario atual ?R$'))
p_101 = 10
p_102 = 20
p_103 = 30
outros = 40
match cargo:
    case '101':
        aumento = (salario_atual * p_101) / 100
        novo_salario = aumento + salario_atual
    case '102':
        aumento = (salario_atual * p_102) / 100
        novo_salario = aumento+salario_atual
    case '103':
        aumento = (salario_atual * p_103) / 100
        novo_salario = aumento+salario_atual
    case 'outros':
        aumento = (salario_atual * outros) / 100
        novo_salario = aumento+salario_atual
    case _:
        cargo = -1
if cargo == -1:
    print('Digite um cargo valido!')
else:
    print(f'Seu salario atual era de R${salario_atual}')
    print(f'Você recebeu um aumento de {aumento}')
    print(f'Seu salario atual é R${novo_salario}')