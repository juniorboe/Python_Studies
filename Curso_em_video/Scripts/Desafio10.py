"""
Crie um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre
quantos dólares ela pode comprar.
USAR A COTAÇÃO DO DIA!
"""

din = float(input('Quantos reais você guarda na carteira: '));
dinDol = din / 4.88;

print('Que legal! Você possui R${:.2f}.\n'
      'Você sabia que dá para comprar ${:.2f} dólares '
      'com o dinheiro que você tem?'.format(din, dinDol));