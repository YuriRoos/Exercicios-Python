soma = 0
idade = 0
cont = 0
maior = 0
for c in range(1, 5):
    print('{} pessoa'.format(c))
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = int(input('sexo: [1] feminino [2] masculino: '))
    soma += idade
    media = soma/4
    if sexo == 1 and idade < 20:
        cont += + 1
    if sexo == 2:
      if idade > maior:
          maior = idade
          nom = nome
    else:
          nome = 'Não tem homem na lista'
print('Média de idade: {}'.format(media))
print('Nome do homem mais velho: {}'.format(nome))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(cont))