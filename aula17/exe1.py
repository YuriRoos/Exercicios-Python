num=int(input('digite um número: '))
tot=0

for c in range(1,num+1):
    if num%c==0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print('\033[31m',end=' ')
    print(f'{c}', end=' ')
 
print(f'\n\033[mO numero {num} foi divisivel {tot} vezes')

if tot==2:
    print('e por isso que ele é primo')
else:
    print('e por isso que ele nao é primo')