din = float(input('Digite o valor do seu saldo no banco: R$'))
credito = 0.0
if din >= 0 and din <= 200:
    credito = 0.0
else:
    if din <= 400:
        credito = (din * 20) / 100
    else:
        if din <= 600:
            credito = (din * 30) / 100
        else:
            credito = (din * 40) / 100
print(f'\nSaldo médio: R${din:.2f}')
print(f'O valor do seu credito é: R${credito:.2f}')
