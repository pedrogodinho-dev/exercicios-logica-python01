valor = int(input("Digite o valor do saque: R$ "))
restante = valor

notas100 = restante // 100
restante %= 100

notas50 = restante // 50
restante %= 50

notas10 = restante // 10
restante %= 10

notas5 = restante // 5
restante %= 5

notas1 = restante
print(f"Valor total: R$ {valor}")

if notas100 > 0:
    print(f'{notas100} nota(s) de R$ 100')
if notas50 > 0:
    print(f'{notas50} nota(s) de R$ 50')
if notas10 > 0:
    print(f'{notas10} nota(s) de R$ 10')
if notas5 > 0:
    print(f'{notas5} nota(s) de R$ 5')
if notas1 > 0:
    print(f'{notas1} moeda(s) de R$ 1')