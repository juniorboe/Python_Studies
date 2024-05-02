"""
Escreva um programa que leia a velocidade
de um carro.

Se ele ultrapassar 80km/h, mostre uma
mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada
Km acima do limite.
"""

v = int(input('Qual a velocidade do carro? ').strip())
multa = (v - 80) * 7

if v > 80:
    print('Velocidade: {}km/h.\n'
          'Você foi multado por excesso de velocidade!\n'
          'Valor: R${:.2f}'.format(v, multa))
else:
    print('Velocidade: {}km/h.'.format(v))