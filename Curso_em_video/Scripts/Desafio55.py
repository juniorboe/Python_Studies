"""
Faça um programa que leia o peso de 
cinco pessoas.

No final, mostre qual 
foi o maior e o menor peso lidos.
"""
maiorPeso = 0
menorPeso = 0
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso digitado é: {}kg.\n'
      'O menor peso digitado é: {}kg.'.format(maiorPeso, menorPeso))
