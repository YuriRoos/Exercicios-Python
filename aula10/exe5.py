camisas=float(input('quantas camisas vai querer levar?'))
valor=float(input('qual o valor das camisas R$:'))

td=camisas*valor


desconto=td*0.97

if desconto <=5:
    print('O valor com o desconto ficara R${:.2f}'.format(desconto))

desconto_b=td*0.95

if desconto_b >=5.1 and desconto_b <10:
    print('O valor com o desconto ficara R${:.2f}'.format(desconto_b))

desconto_c=td*0.93

if desconto_c >10.1:
    print('O valor com o desconto ficara R${:.2f}'.format(desconto_c))
