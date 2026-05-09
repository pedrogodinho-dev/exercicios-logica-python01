a = int(input('Digite um numero inteiro: '))
b = int(input('Digite outro numero inteiro: '))
c = int(input('Digite outro numero inteiro: '))
res = ''
if a > b and a > c:
    if b > c:
        res = c
    else:
        res = b
else:
    if b > a and b > c:
        if a > c:
            res = c
        else:
            res = a
    else:
        if b > a:
            res = a
        else:
            res = b
print(f'O menor número digitado foi {res}')
