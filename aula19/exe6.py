primeiro=int(input('primeiro termo: '))
razao=int(input('razao da PA: '))
termo=primeiro 
cont=1
while cont<=10:
    print(f'{termo}', end=' ')
    termo+=razao
    cont+=1
print('Fim')

resp=' '  

while resp not in 'SN':
    resp=input('quer mostrar mais algum termo? [S/N]? ').strip().upper()
    
    if resp=='N':
        break

    while True:
        primeiro=int(input('primeiro termo: '))
        razao=int(input('razao da PA: '))
        termo=primeiro 
        cont=1
        while cont<=10:
            print(f'{termo}', end=' ')
        termo+=razao
        cont+=1
        if primeiro == 0:
            break
