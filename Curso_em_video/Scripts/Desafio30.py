"""
Crie um programa que leia um número
inteiro e mostre na tela se ele
é par ou ímpar
"""

n = int(input('Digite um número: ').strip())

if n % 2:
    print('ÍMPAR!')
else:
    print('PAR!')