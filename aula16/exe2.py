soma=0

medicamento=input('medicamento: ')
preco = float(input('informe o preço do medicamento: '))

maisbarato=medicamento
menorpreco=preco
    
soma+=preco

for x in range(4):
    medicamento=input('medicamento: ')
    preco = float(input('informe o preço do medicamento: '))
    if preco<menorpreco:
        menorpreco=preco
        maisbarato=medicamento
    soma+=preco
media=soma/5

print(f'{maisbarato} é o medicamento mais barato e custa R$ {menorpreco} \n media dos precos: {media}')


