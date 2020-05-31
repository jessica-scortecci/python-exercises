from time import sleep
print('='*40)
print('          CALCULADORA LIMITADA')
print('='*40)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

opcao = 0
while opcao != 5:
    print('''
MENU:
[1] Somar
[2] Multiplicar 
[3] Maior número
[4] Digitar novos números
[5] SAIR
    ''')
    opcao = int(input('>>>>>> Escolha uma das opções acima: '))
    if opcao == 1:
        print('A soma é igual a {}.'.format(n1 + n2))
    elif opcao == 2:
        print('A multiplicação é igual a {}.'.format(n1 * n2))
    elif opcao == 3:
        if n1 == n2:
            print('Não há número maior. Os dois números são iguais.')
        elif n1 > n2:
            print('O número {} é maior que {}.'.format(n1, n2))
        else:
            print('O número {} é maior que {}.'.format(n2, n1))
    elif opcao == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente...')
    print('=-=-=-'*6)
    sleep (2)
    
print('UFA... acabou!')
