from random import randint

n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('os valores sorteados foram: ', end='')
for num in n:
    print(f'{n}', end='')
print(f'o maior valor sorteado foi {max(n)}')
print(f'o menor valor sorteado foi {min(n)}')

'''print(n)'''