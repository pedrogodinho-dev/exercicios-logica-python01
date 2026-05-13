print('=' *25 + 'COFRE DIGITAL' + '=' *25 )
print('\nDIGITE 1:Para entrar com a biometria')
print('DIGITE 2:Para entrar com login e senha')
print('DIGITE 3:Para sair')
print('\n' + '='*63)
forma_acesso = input('Digite a forma que deseja entrar: ')
biometria = 'bombom_caribe'
login = 'admin'
senha = '1234'
match forma_acesso:
    case '1':
        bio = input('Digite a sua biometria: ')
        if bio == biometria:
            print('Acesso permitido. Cofre aberto.')
        else:
            print('Acesso negado. Biometria incorreta.')
    case '2':
        log = input('Digite a seu login: ')
        sen = input('Digite a sua senha: ')
        if log == login and sen == senha:
            print('Acesso permitido. Cofre aberto.')
        else:
            print('Acesso negado. Login ou senha incorretas.')
    case '3':
        print('Sistema encerrado.')
    case _:
        print('Opção invalida. Tente novamente.')