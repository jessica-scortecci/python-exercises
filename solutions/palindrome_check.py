frase = str(input('Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]

if inverso == junto:
    print('A frase "{}" é um palíndromo.'.format(frase))
else:
    print('A frase "{}" NÃO é um palíndromo.'.format(frase))
