lista = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    
    if pessoa['Sexo'] not in 'MF':
        print('ERRO. Por favor, digite apenas M ou F.')
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    lista.append(pessoa.copy())

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp not in 'SN':
        print('ERRO. Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-'*30)

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')

media = soma / len(lista)
print(f'B) A média de idade é de {media:.2f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f' {p["Nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')

'''
for v in lista:
    if v['Idade'] >= media:
        print(f'Nome = {v["Nome"]}; Sexo = {v["Sexo"]}; Idade = {v["Idade"]}')
'''

for p in lista:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
print('<<<    ENCERRADO    >>>')
