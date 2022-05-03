from random import shuffle,choice

rifa=[]

while True:
    nome = input('Nome: ')
    rifa.append(nome)
    resp=input('deseja continuar [S/N]: ')    
    if resp.upper() == 'N':
        break

shuffle(rifa)
sorteado=choice(rifa)


print(f'O ganhador da rifa foi o(a) {sorteado}')