from random import randint

itens = ['pedra','papel','tesoura']
computador=randint(0,2)
print('suas opçoes sao:[0] pedra [1] papel [2] tesoura')

jogador=int(input('qual sua jogada:'))

print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('VENCEU')

    elif jogador == 2:
        print('PERDEU')
    
    else:
        print('jogada invalida')
    
if computador == 1:
    if jogador == 0:
        print('PERDEU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('GANHOU')

    else:
        print('jogada invalida')

if  computador == 2:
    if jogador == 0:
        print('GANHOU')

    elif jogador == 1:
        print('PERDEU')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('jogada invalida')

