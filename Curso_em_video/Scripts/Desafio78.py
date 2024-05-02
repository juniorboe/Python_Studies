"""
Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista.

No final, mostre qual foi o maior e o menor valor
digitado e as suas respectivas posições na lista.
"""

lista = list()
for i in range(0, 5):
    lista.append(int(input('Digite um número: ')))

maior = lista[0]
posMaior = 0
menor = lista[0]
posMenor = 0
for i, c in enumerate(lista):
    if c > maior:
        maior = c
        posMaior = i
    if c < menor:
        menor = c
        posMenor = i
print(f'Lista: {lista}.')
print(f'O maior número é {maior}, e está na posição {posMaior + 1}.')
print(f'O menor número é {menor}, e está na posição {posMenor + 1}.')
    
