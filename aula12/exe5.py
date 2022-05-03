from math import sqrt

x1=float(input('digite o valor de x1:'))
y1=float(input('digite o valor de y1:'))

x2=float(input('digite o valor de x2:'))
y2=float(input('digite o valor de y2:'))

x3=float(input('digite o valor de x3:'))
y3=float(input('digite o valor de y3:'))

l1=sqrt(pow(x2-x1,2)+pow(y2-y1,2))
l2=sqrt(pow(x3-x1,2)+pow(y3-y1,2))
l3=sqrt(pow(x3-x2,2)+pow(y3,y2,2))

cond1 = True 
cond2 = True
cond3 = True 

if l1==0 or l2==0 or l3==0:
    cond1=False

if l1>(l2+l3) or l2>(l1+l3) or l3>(l1+l2):
    cond2=False

if l1<=abs(l2-l3) or l2<=abs(l1-l3) or l3<=abs(l1-l2):
    cond3=False

triangulo=True

if cond1==False or cond2==False or cond3==False:
    traingulo=False
    print('Nenhum triangulo formado!')

if cond1==False:
    print('pelo meno um dos lados é igul á 0!')

if cond2==False:
    print('pelo menos um lado é maior que a soma dos outros dois!')

if cond3==False:
    print('um dos lados é menor ou igual ao modulo da diferença!')

elif l1==l2==l3:
    print('triangulo equilatero.')

elif l1!=l2!=l3:
    print('triangulo é escaleno')

else:
    print('traingulo é isóceles')

if triangulo:
    print('medida do lado 1: {:.2f} \n medida do lado 2:{:.2f} \n medida do lado 3:{:.2f}'.format(l1,l2,l3))