lista=[12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
maiorvalor=lista[0]
menorvalor=lista[0]
listapares=[]
ocorrencia=0
mediaelementos=0
somanegativo=0

for index in range(0,len(lista)):
    #maior valor
    if maiorvalor<lista[index]:
        maiorvalor=lista[index]
    #menor valor
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    #pares
    if lista[index]%2==0:
        listapares.append(lista[index])
    #elementos
    if lista[index]==lista[0]:
        ocorrencia+=1
    #media
    mediaelementos+=lista[index]
    mediaelementos/=len(lista)
    #soma numeros negativos
    if lista[index]<0:
        somanegativo+=lista[index]

print(f'maior valor é: {maiorvalor} ')
print(f'maior valor é: {menorvalor} ')
print(f'lista de numeros pares: {listapares}')
print(f'numero de ocorencias do primeiro elemento: {ocorrencia}')
print(f'media dos elementos: {mediaelementos}')
print(f'elementos negativos: {somanegativo}')