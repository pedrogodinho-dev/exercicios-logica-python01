nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media < 4:
    conceito = 'E'
else:
    if media < 6:
        conceito = 'D'
    else:
        if media < 7.5:
            conceito = 'C'
        else:
            if media < 9:
                conceito = 'B'
            else:
                conceito = 'A'
print(f'A media calculada é: {media:.2f} e o conceito é: {conceito}')