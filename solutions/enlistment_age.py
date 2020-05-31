from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
