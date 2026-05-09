pontos = [120,85,150,60,95,200,110,70]
cemOuMais = 0
menosDeCem = 0
totalPontos = 0
jogadoresEntre80E150 = 0
quantidadeDeJogadores = 0
for i in pontos:
    quantidadeDeJogadores +=1
    totalPontos +=i
    if i > 100:
        cemOuMais +=1
    else:
        menosDeCem +=1
    if i >=80 and i <=150:
        jogadoresEntre80E150 +=1
print(f'Jogadores com mais de 100 pontos: {cemOuMais}')
print(f'Jogadores com menos de 100 pontos: {menosDeCem}')
print(f'Jogadores entre 80 e 150 pontos: {jogadoresEntre80E150}')
print(f'Pontuação total: {totalPontos}')
media = totalPontos/quantidadeDeJogadores
posicaoMaior = 0
posicaoMenor = 0
maiorValor = pontos[0]
menorValor = pontos[0]
listaAcimaMedia = []
primeiraPosicaoAcima = -1
for x in range(quantidadeDeJogadores):
    if pontos[x] > maiorValor:
        maiorValor = pontos[x]
        posicaoMenor = x
    if pontos[x] < menorValor:
        menorValor = pontos[x]
        posicaoMenor = x
    if pontos[x]>media:
        listaAcimaMedia.append(pontos[x])
        if primeiraPosicaoAcima == -1:
            primeiraPosicaoAcima = x
print(f'Pontuação média: {media:.2f}')
print(f'Pontuações acima da média: {listaAcimaMedia}')
print(f'Posição do maior jogador: {posicaoMaior} (Valor: {maiorValor})')
print(f'Posição do menor jogador: {posicaoMenor} (Valor: {menorValor})')
print(f'Posição do primeiro jogador acima da média: {primeiraPosicaoAcima}')