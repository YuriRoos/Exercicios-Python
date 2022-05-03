soma = 0
for c in range(1, 6):
    num = int(input('Número:'))
    if num % 2 == 0:
        soma+=1
print('o total de números pares é {}'.format(soma))