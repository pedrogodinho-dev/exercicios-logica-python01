a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite outro numero: '))

if a > b and a > c:
    if b > c:
        print(a + b)
    else:
        print(a + c)
else:
    print(b + c)
