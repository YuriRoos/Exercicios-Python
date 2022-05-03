peso=float(input('digite o seu peso:'))
altura=float(input('digite sua altura(em metros):'))

imc=peso/altura**2

if imc <=18.5:
    print('ABAIXO DO PESO!')

elif imc >=18.6 and imc <25:
    print('PESO IDEAL!')

elif imc >=25.1 and imc <30:
    print('SOBREPESO!')

elif imc >=30.1 and imc <40:
    print('OBESIDADE!')

else:
    print('OBESIDADE MÓRBITA!')