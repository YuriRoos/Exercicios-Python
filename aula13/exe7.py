s=str(input('digite seu sexo [M/F]:')).strip().upper()
while s!= 'M' and s!= 'F':
    print('Você não digitou da forma correta')
    s=str(input('digite seu sexo [M/F]:')).strip().upper()
print('seu sexo é {}'.format(s))
    