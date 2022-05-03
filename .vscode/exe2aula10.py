n1=float(input('primeiro segmento:'))
n2=float(input('segundo segmento:'))
n3=float(input('terceiro segmento:'))

if n1<n2+n3 and n2<n1+n2 and n3<n1+n2:
    print('o segmentos acima podem formar um triangulo')
    if n1==n1 and n2==n3 and n3==n1:
        print('equilatero')
    elif n1!=n2 and n1!=n3 and n2!=n1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('os segmentos acima nao podem formar um triangulo')
