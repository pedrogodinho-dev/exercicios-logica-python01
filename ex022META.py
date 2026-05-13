time1 = input('Digite o nome do primeiro time: ')
time2 = input('Digite o nome do segundo time: ')
gol_time1 = int(input(f'Quantos gols o {time1} time fez ?'))
gol_time2 = int(input(f'Quantos gols o {time2} time fez ?'))
if gol_time1 > gol_time2:
    print(f'O time {time1} ganhou o jogo de {gol_time1} a {gol_time2}')
else:
    if gol_time1 == gol_time2:
        print(f'O jogo empatou de {gol_time1} a {gol_time2}!')
    else:
         print(f'O time {time2} ganhou o jogo de {gol_time2} a {gol_time1}')