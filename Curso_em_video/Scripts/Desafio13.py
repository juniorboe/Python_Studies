"""
Faça um algoritmo que leia o salário
de um funcionário e mostre seu novo
salário, com 15% de aumento.
"""

salario = float(input('Digite o salário atual do funcionário: '));

salComA = salario * 1.15;

print('O salário do funcionário com aumento de 15% é: R${:.2f}.'.format(salComA));