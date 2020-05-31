from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Vamos jogar Jokenpô?')
jogador = int(input('Estas são as opções: \n[ 0 ] Pedra \n[ 1 ] Papel \n[ 2 ] Tesoura \nQual é a sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 11)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida.')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida.')
elif computador == 2:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida.')
