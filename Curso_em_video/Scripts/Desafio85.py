"""
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores
pares e ímpares. No final, mostre os valores pares e ímpares em 
ordem crescente.
"""

numeros = [[], []]

for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
if len(numeros[0]) > 0:
    numeros[0].sort()
    print(f'Os valores pares em ordem crescente são: {numeros[0]}')
else:
    print('Nenhum número par foi digitado.')
if len(numeros[1]) > 0:
    numeros[1].sort()
    print(f'Os valores ímpares em ordem crescente são: {numeros[1]}')
else:
    print('Nenhum número ímpar foi digitado.')
