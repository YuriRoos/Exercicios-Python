n1=int(input('primeiro valor: '))
n2=int(input('segundo valor: '))

opcao=0

while opcao != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')
    opcao=int(input('qual é a sua opçao: '))

    if opcao == 1:
        soma=n1+n2
        print(f'a soma entre {n1} e {n2} : {soma}')
    elif opcao == 2:
        produto=n1*n2
        print(f'o produto entre {n1} e {n2} : {produto}')
    elif opcao == 3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print(f'entre {n1} e {n2} o maior valor é : {maior} ')
    elif opcao == 4:
        print('informe novos numeros: ')
        n1=int(input('primeiro numero: '))
        n2=int(input('segundo numero: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('opçao invalida')
    print ('#'*10)

print('FIM')
