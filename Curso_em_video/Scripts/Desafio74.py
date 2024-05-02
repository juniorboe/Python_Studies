"""
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e 
também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'A listagem de números é: {numeros}')
numerosOrdenados = sorted(numeros)
print(f'O menor valor da listagem é: {numerosOrdenados[0]}')
print(f'O maior valor da listagem é: {numerosOrdenados[len(numerosOrdenados) - 1]}')      
