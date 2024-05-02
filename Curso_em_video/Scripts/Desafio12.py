"""
Faça um algoritmo que leia o preço
de um produto e mostre seu novo preço,
com 5% de desconto.
"""

price = float(input('Digite o preço do produto: '));

desPrice = price * 0.95;

print('Preço do produto: R${:.2f}.\n'
      'Preço atual do produto com desconto: R${:.2f}.'.format(price, desPrice));