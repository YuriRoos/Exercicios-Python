from operator import truediv
from random import randint
computador=randint(0,10)
print('vou pensar em um numero de 0 a 10 tente adivinhar')

acertou=False
palpite=0

while not acertou:
    jogador=int(input('em que numero estou pensando: '))
    palpite+=1
    if jogador==computador:
        acertou=True
    else:
        if jogador<computador:
            print('mais ... tente novamente!')
        elif jogador>computador:
            print('menos ... tente novamente!')
print('acertou com {} tentativas. Parabéns! '.format(palpite))










