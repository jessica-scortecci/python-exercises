from random import randint
from time import sleep
from operator import itemgetter

jogador = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
ranking = list()

print('Valores sorteados: ')
print()
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print('=-'*15)
print()
print('=== RANKING DOS JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'{i+1}o. lugar: {v[0]} com {v[1]}.')
    sleep(1)
