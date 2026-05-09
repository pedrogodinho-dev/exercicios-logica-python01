num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 % num2 == 0 or num2 % num1 == 0:
    print('São multiplos')
else:
    print('Não são multiplos')