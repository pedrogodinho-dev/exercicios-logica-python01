idade = int(input('Digite a sua idade: '))
res = ''
if idade < 5:
    res = 'Ainda nao possui categoria'
else:
    if idade <= 7 and idade >= 5:
        res = 'categoria infantil A'
    else:
        if idade <= 10:
            res = 'categoria infantil B'
        else:
            if idade <= 13:
                res = 'categoria juvenil A'
            else:
                if idade <=17:
                    res = 'categoria juvenil B'
                else:
                    if idade >= 18:
                        res = 'categoria adulto'
print(f'Com base na sua idade: {idade}, {res}')