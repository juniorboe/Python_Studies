"""
Desenvolva um programa que leia o
comprimento de três retas e diga ao
usuário se elas podem ou não formar um
triângulo

Condição de existência: um de seus lados
deve ser menor que a soma desses dois lados
"""

l1 = float(input('Digite o comprimento do lado 1: ').strip())
l2 = float(input('Digite o comprimento do lado 2: ').strip())
l3 = float(input('Digite o comprimento do lado 3: ').strip())

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Pode ser uma reta!')
else:
    print('Não pode ser uma reta!')

