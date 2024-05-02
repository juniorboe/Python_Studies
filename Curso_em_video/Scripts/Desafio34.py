"""
Escreva um programa que pergunte o 
salário de um funcionário e calcule
o valor do seu aumento.

Para salários superiores a R$1.250,00,
calcule um aumento de 10%

Para os inferiores ou iguais, o aumento
é de 15%
"""

salario = float(input('Digite o salário do funcionário: ').strip())

if salario > 1250:
    salarioAum = salario * 1.10
    print('Novo salário: R${:.2f}'.format(salarioAum))
else:
    salarioAum = salario * 1.15
    print('Novo salário: R${:.2f}'.format(salarioAum))