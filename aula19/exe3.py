media=0
maior=0
menor=0
count=0
soma=0

while True:
    n=int(input('numero: '))

    if n == n:
        count+=n
        soma+=n
    
    if  n > maior:
        maior = n
    if  n < menor:
        menor = n
     
    resp=' '  
    
    while resp not in 'SN':
        resp=input('quer continuar [S/N]? ').strip().upper()
    media=soma/count
  
    if resp=='N':
        break
    
print('a media entre esses numeros é {}\n o menor numero é {}\n o maior numero é {}'.format(media,menor,maior))
