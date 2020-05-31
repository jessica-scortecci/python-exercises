from datetime import date
atual = date.today().year

maior = 0
menor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}a pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('No total tivemos {} pessoas maiores de idade.'.format(maior))
print('E também {} pessoas menores de idade.'.format(menor))
