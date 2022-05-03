soma=0
count=0

while True:
    n=int(input('numero: '))

    if n != 999:
        count+=1
        soma+=n

    elif n == 999:
        print('Acabou')
        break

print('foram digitados {} numeros e a soma entre eles é {}'.format(count,soma))
