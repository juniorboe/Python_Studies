"""
Escreva um programa que leia um valor
em metros e o exiba convertido em
centímetros e milímetros.
"""

valMet = int(input('Digite um valor: '));

valCen = valMet * 100;
valMil = valMet * 1000;

print('O valor em metros digitado é: {}m.\n'
      'Valor em centímetros: {}cm.\n'
      'Valor em milímetros: {}mm.'.format(valMet, valCen, valMil));