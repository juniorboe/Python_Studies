"""
Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e
raiz quadrada.
"""

num = int(input('Digite um número: '));

doub = num * 2;
trip = num * 3;
rquad = num ** (1/2);

print('O número é: {}.\n'
      'O seu dobro é: {}.\n'
      'O seu triplo é: {}.\n'
      'A sua raiz quadrada é: {}.'.format(num, doub, trip, rquad));