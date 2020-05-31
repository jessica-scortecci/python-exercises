a = float(input('Digite a medida da reta a: '))
b = float(input('Digite a medida da reta b: '))
c = float(input('Digite a medida da reta c: '))
if a < b + c and b < a + c and c < a + b:
#if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Com medidas das retas a = {}, b = {} e c = {}, é possível formar um triângulo.'.format(a, b, c))
    if a == b == c:
        print('O triângulo formato é EQUILÁTERO.')
    elif a != b != c != a:
        print('O triângulo formado é ESCALENO.')
    else:
        print('O triângulo formato é ISÓSCELES.')
else:
    print('Com as medidas das retas a = {}, b = {} e c = {}, NÃO é possível format um triângulo.'.format(a, b, c))
