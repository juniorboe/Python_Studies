"""
Desenvolva um programa que pergunte a
distância de uma viagem em Km.
Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de até
200km e R$0,45 para viagens mais longas.
"""

distancia = int(input('Qual a distância da sua viagem? ').strip())

if distancia <= 200:
    valor = distancia * 0.5
    print('Distância a percorrer: {}km.\n'
          'Valor: R${}.'.format(distancia, valor))
else:
    valor = distancia * 0.45
    print('Distância a percorrer: {}km.\n'
          'Valor: R${}.'.format(distancia, valor))
    