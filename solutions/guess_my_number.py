from random import randint
comp = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi...')

acertou = 'errou'
palpites = 0
while acertou == 'errou':
    jogador = int(input('Qual o seu palpite: '))
    palpites += 1
    if jogador == comp:
        acertou = 'acertou'
    else:
        if jogador < comp:
            print('Mais... Tente mais uma vez.')
        elif jogador > comp:
            print('Menos... Tente mais uma vez.')
print('Acertou! Foram necessários {} palpites até você acertar.'.format(palpites))
