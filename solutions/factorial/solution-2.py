n = int(input('Fatorial de: '))
r = 1
cont = 1
while cont <= n:
    r = r * cont
    cont+= 1
print('O fatorial de {} é {}.'.format(n, r))
