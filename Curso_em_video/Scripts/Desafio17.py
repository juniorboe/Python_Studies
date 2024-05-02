"""
Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e 
mostre o comprimento da hipotenusa
"""

import math;

catO = float(input('Digite o valor do cateto oposto: '));
catA = float(input('Digite o valor do cateto adjacente: '));

hip = math.hypot(catO, catA);

print('O comprimento da hipotenusa é: {:.3}'.format(hip));