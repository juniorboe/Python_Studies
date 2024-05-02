"""
Escreva um programa que leia dois números
inteiros e compare-os, mostrando na tela
uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

num1 = float(input('Digite o primeiro valor: ').strip())
num2 = float(input('Digite o segundo valor: ').strip())

if num1 > num2:
    print('\033[1;32mO primeiro valor é maior.\033[m\n'
          'Primeiro valor: {}.\n'
          'Segundo valor: {}.'.format(num1, num2))
elif num2 > num1:
    print('\033[1;32mO segundo valor é maior.\033[m\n'
          'Primeiro valor: {}.\n'
          'Segundo valor: {}.'.format(num1, num2))
else:
    print('\033[1;33mOs dois valores são iguais!\033[m\n'
          'Primeiro valor: {}.\n'
          'Segundo valor: {}.'.format(num1, num2))
