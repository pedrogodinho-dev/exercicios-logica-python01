indice = float(input('Qual é o indice de poluição: '))
if indice >= 0.5:
    print('As industrias dos grupos 1, 2 e 3 devem paralisar suas atividades.')
else:
    if indice >= 0.4:
        print('As industrias dos grupos 1 e 2 devem ser notificadas.')
    else:
        if indice >= 0.3:
            print('As industrias dos grupos 1 devem ser notificadas.')
        else:
            print(f'O nivel está dentro do aceitavel!')