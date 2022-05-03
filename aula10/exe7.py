sal=float(input('informe seu salario:'))

print('cargo [1] (programador de sistemas)')
print('cargo [2] (analista de sistemas)')
print('cargo [3] (analista de banco de dados)')

a=str(input('informe seu cargo:'))

if a == '1':
    b=sal*0.30
    print('voce recebera o salario de R${} a mais'.format(b))

elif a == '2':
    c=sal*0.20
    print('voce recebera o salario de R${} a mais'.format(c))

elif a == '3':
    d=sal*0.15
    print('voce recebera o salario de R${} a mais'.format(d))

else:
    print('Voce nao se emquadra em nenhum desses cargos!')
    
