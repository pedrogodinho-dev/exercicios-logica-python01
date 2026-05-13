nota = float(input('Diga sua nota numerica: '))
grau = ''
if nota < 0 or nota > 100:
    print('Nota invalida! ')
else:
    if nota < 50:
        grau = 'F'
    else:
        if nota < 60:
            grau = 'E'
        else:
            if nota < 70:
                grau = 'D'
            else:
                if nota < 80:
                    grau = 'C'
                else:
                    if nota < 90:
                        grau = 'B'
                    else:
                        grau = 'A'
print(f'Seu grau de nota é {grau}')