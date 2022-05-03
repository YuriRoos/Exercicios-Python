v1=int(input('informe um valor: '))
v2=int(input('informe um valor: '))
v3=int(input('informe um valor: '))
v4=int(input('informe um valor: '))

lista=(v1,v2,v3,v4)

a=(lista.count(9))
print(f'o valor 9 apareceu {a} vez(s)')

if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

print('Os valores pares digitados foram ', end=' ')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')