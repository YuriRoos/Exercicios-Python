N=int(input("Quantos elementos exibir: ") )
soma=0

for c in range(0,N):
    num=float(input('digite um numero: '))
    soma=soma+num
media=soma/N
print('a media aritmetica é {:.2f}'.format(media))
    