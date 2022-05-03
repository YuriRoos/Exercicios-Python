print('codigo de cargo \n1 : enfermeiro \n2 : nutricionista \n3 : medico')

qtdenutri=0
totalsalnutri=0

while True:
    cargo=int(input('informe um cargo: '))
    if cargo>=1 and cargo<=3:
        salario=float(input('salario R$: '))
        if cargo ==2:
            qtdenutri+=1
            totalsalnutri+=salario
        resp=int(input('deseja continuar [S/N]: '))
        if resp.upper()=='N':
            break
    
    else:
        print('Codogo invalido')

if qtdenutri>0:
    media=totalsalnutri/qtdenutri
    print(f'media salarial das nutricionistas R$: {media:.2f}')

else:
    print('nao foram inseridos dados sobre as nutricionistas')



