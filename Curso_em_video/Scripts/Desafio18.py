"""
Faça um programa que leia um ângulo
qualquer e mostre na tela o valor do
seno, cosseno e tangente desse ângulo
"""
from math import sin, cos, tan, radians;

angulo = int(input('Digite um ângulo: '));

seno = sin(radians(angulo));
coss = cos(radians(angulo));
tang = tan(radians(angulo));

print('O ângulo digitado foi: {}.\n'
      'O seu seno é {:.2f}.\n'
      'O seu cosseno é {:.2f}.\n'
      'A sua tangente é {:.2f}.'.format(angulo, seno, coss, tang));