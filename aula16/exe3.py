nome=input('informe seu nome: ')

for c in range (3,0,-1):
    senha=int(input('informe a senha do usuario: '))
    if senha == 123456:
        print('Olá {} seja bem-vindo ao nosso banco!'.format(nome))
        break
    elif senha != 123456:
        print('senha incorreta você ainda tem 2 tentativas!')
        
    elif senha != 123456:
        print('senha incorreta você ainda tem 1 tentativa!')
        
    elif senha != 123456:
        print('sua senha foi bloqueada! por favor dirija-se a um de nossos caixas!')
        break


