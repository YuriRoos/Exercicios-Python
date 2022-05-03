p1=input('estatura da pessoa 1:')
p2=input('estatura da pessoa 2:')
p3=input('estatura da pessoa 3:')



if p1>p2 and p2>p3:
    print('Ordem decrescente {},{},{}'.format(p1,p2,p3))

if p1>p3 and p3>p2:
    print('Ordem decrescente {},{},{}'.format(p1,p3,p2))

if p2>p1 and p1>p3:
    print('Ordem decrescente {},{},{}'.format(p2,p1,p3))

if p2>p3 and p3>p1:
    print('Ordem decrescente {},{},{}'.format(p2,p3,p1))

if p3>p1 and p1>p2:
    print('Ordem decrescente {},{},{}'.format(p3,p1,p2))

if p3>p2 and p2>p3:
    print('Ordem decrescente {},{},{}'.format(p3,p2,p1))
