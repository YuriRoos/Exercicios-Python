from math import sqrt

lista=[9,3,5,7,2,1]

menor=min(lista)
maior=max(lista)
media_geo=sqrt(menor*maior)

print(f'lista: {lista}')
print(f'media geometrica entre {menor} e o {maior} elemento é igual a {media_geo}')