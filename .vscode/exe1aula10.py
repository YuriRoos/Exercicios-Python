from datetime import date
from inspect import isdatadescriptor

atual=date.today().year
nascimento=int(input('ano de nascimento:'))
idade=atual - nascimento
print('o atleta tem {} anos.'.format(idade))

if idade <=9:
    print('Voce esta na categoria mirim!')

elif idade  <=14:
    print('Voce esta na categoria infantil!')

elif idade  <=19:
    print('Voce esta na categoria junior!')

elif idade  <=25:
    print('Voce esta na categoria senior!')

else:
    print('Voce esta na categoria master!')
