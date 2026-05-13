a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota: '))
d = float(input('Digite a quarta nota: '))

media = (a + b + c + d) / 4
if media < 3:
    conceito = 'R'
else:
    if media < 7:
        conceito = 'E'
    else:
        conceito = 'A'
print(f'A media foi de: {media} e o conceito foi de: {conceito}')