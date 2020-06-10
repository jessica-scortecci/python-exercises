print('-'*35)
print('         CAIXA ELETRÔNICO')
print('-'*35)

valor = int(input('Valor a sacar: R$'))
total = valor
cedula = 50
totalcedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedulas += 1
    else:
        if totalcedulas > 0:
            print(f'Total de {totalcedulas} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedulas = 0
        if total == 0:
            break
print('-'*35)
print('Obrigado. Volte sempre.')
