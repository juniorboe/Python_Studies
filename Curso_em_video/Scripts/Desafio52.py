"""
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
"""
import time

num = int(input('Digite um número: ').strip())
tot = 0
print('Verificando se o número digitado é primo...')
time.sleep(1)
for i in range(1, num + 1):
    if num % i == 0:
        tot += 1
if tot == 2:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))
