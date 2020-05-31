casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário mensal: R$ '))
anos = int(input('Quantos anos deseja financiar: '))
prestacao = casa / (anos * 12)
if prestacao <= (salario * 30 / 100):
    print('Seu financiamento foi aprovado. \nVocê irá pagar {} prestações no valor de R${:.2f}.'.format((anos * 12), prestacao))
else:
    print('O valor da prestação é de R${:.2f} e excede 30% do seu salário mensal. \nInfelizmente seu financiamento não foi aprovado.'.format(prestacao))
