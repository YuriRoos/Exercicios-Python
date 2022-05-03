media=0
maior=0
menor=0
count=0
soma=0

while True:
    n=float(input('Altura: '))

    if n == n:
        count+=n
        soma+=n
        media=soma/count
    if  n > maior:
        maior = n
    if  n < menor:
        menor = n
     
    resp=' '  
    
    while resp not in 'SN':
        resp=input('quer continuar [S/N]? ').strip().upper()
    
    if resp=='N':
        break
    
print('a media entre as alturas dos alunos é {}\n a menor altura é {}\n a maior altura é {}'.format(media,menor,maior))
