sexo=0
idade=0
mulher=0
homem=0

while True:
    idade=int(input('informe a idade do aluno: '))   
    if idade<0:
        break
    sexo=input('sexo: ').upper()
    if sexo=='F':
        mulher+=1
    elif sexo== 'M' and idade>18:
        homem+=1
print(f'total de mulheres: {mulher} \nTotal de homens: {homem}')

    


    

    
