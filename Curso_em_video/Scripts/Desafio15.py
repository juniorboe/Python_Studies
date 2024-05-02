"""
Escreva um programa que pergunte a 
quantidade de Km percorridos por um carro
alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço
a pagar, sabendo que o carro custa
R$60 por dia e R$0,15 por Km rodado.
"""

dias = float(input('Quantos dias o carro foi alugado? '));
km = float(input('Quantos km o carro rodou? '));

preço = (60 * dias) + (0.15 * km);

print('Custo do aluguel: {}'.format(preço));