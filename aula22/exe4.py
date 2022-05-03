n = int(input('digite um numero impar,maior que 1: '))

if n<=1 or n%2 == 0:
    print(f'Numero informado nao atende os criterios definidos')
else:
    l=[]
    for x in range(n):
        num=int(input(f'digite um numero maior ou igual a 0: '))
        l.append(num)

centro=int(len(l)/2)
elementocentro=l[centro]
fatorial=1

for n in range(2,elementocentro+1):
    fatorial*=n
print(f'lista: {1}')
print(f'o elemento do centro da lista {elementocentro} e seu fatorial é igual a {fatorial}')

