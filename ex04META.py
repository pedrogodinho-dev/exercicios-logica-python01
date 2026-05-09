nota1 = float(input('Primeiro valor: '))
nota2 = float(input('Segundo valor: '))
nota3 = float(input('Terceiro valor: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'O aluno foi APROVADO! a media dele é {media:.2f}')
else:
    print(f'O aluno foi REPROVADO! a media dele é {media:.2f}')