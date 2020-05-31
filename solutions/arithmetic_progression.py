print('='*30)
print('    10 TERMOS DE UMA PA    ')
print('='*30)

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n10 = n1 + (10 - 1) * r     # para descobrir o décimo termo da PA

for c in range(n1, n10 + r, r):
    print('{}'.format(c), end=' -> ')
print('ACABOU!')
