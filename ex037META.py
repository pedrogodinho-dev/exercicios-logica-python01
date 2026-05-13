ano_atual = int(input('Qual o ano atual ?'))
ano_nasc = int(input('Qual seu ano de nascimento ?'))

idade = ano_atual - ano_nasc
if idade >= 16:
    print(f'Você tem {idade} anos. Já pode votar!')
else:
    print(f'Você tem {idade} anos. Ainda não pode votar!')