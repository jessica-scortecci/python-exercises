n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter pata OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
