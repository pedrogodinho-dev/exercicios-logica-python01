cod = (input('Digite o seu codigo: '))

a = float(input('Digite a primeira nota: '))
pesoA = 3
b = float(input('Digite a segunda nota: '))
pesoB = 3
c = float(input('Digite a terceira nota: '))
pesoC = 4
media = (a * pesoA + b * pesoB + c * pesoC) / (pesoA + pesoB + pesoC)
if media >= 5:
    print(f'Aluno com o codigo:{cod} você foi APROVADO! sua media é: {media:.2f}')
else:
    print(f'Aluno com o codigo:{cod} foi REPROVADO! sua media é: {media:.2f}')

