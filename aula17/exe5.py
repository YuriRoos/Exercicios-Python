total=totmil=menor=cont=0

barato=' '
while True:
    produto=input('nome do produto: ')
    preco=float(input('preço R$: '))
    cont+=1
    total+preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resp=' '
    while resp not in 'SN':
        resp=input('quer continuar [S/N]? ').strip().upper()
    if resp=='N':
        break
print(f'o total das compras foi R${total:.2f}')
print(f'temos {totmil} produtos custando mais de 1000R$')
print('o produto mais barato foi o {produto} que custa R${menor:.2f}')
