frase=input('digite a frase: ')
caracter=input('digite o caracter que busca: ')

qtde=0

for c in frase:
    if c.lower()==caracter.lower():
        qtde+=1
    
print('o caracter apareceu {} vezes na frase'.format(qtde))