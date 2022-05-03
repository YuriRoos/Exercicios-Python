pro=float(input('informe o valor do produto R$:'))

print('------------------\nqual a forma de pagamento\n--------------------------')
print('cheque [1]')
print('cartao [2]')
print('cartao2x [3]')

a=str(input('comfirme a forma de pagamento:'))

if a == '1':
    cheque=pro*0.90
    print('o valor do produto ficara R${:.2f}'.format(cheque))

elif a == '2':
    cartao=pro*0.95
    print('o valor do produto com o desconto ficara R${:.2f}'.format(cartao))

elif a == '3':
    cartao2x=pro
    print('o valor do produto ficara R${:.2f}'.format(cartao2x))