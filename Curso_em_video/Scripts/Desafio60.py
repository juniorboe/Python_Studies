"""
Faça um programa que leia um número qualquer
e mostre o seu falorial.

Ex:
 5! = 5x4x3x2x1 = 120
"""

num = int(input('Digite um número: '))
resultado = num
count = num - 1

while count > 0:
    resultado *= count
    count -= 1
print('O fatorial de {} é: {}.'.format(num, resultado))
"""
ou

num = int(input('Digite um número: '))
resultado = 1
count = 1
while count <= num:
    resultado *= count
    count += 1
print('O fatorial de {} é: {}.'.format(num, resultado))
"""

