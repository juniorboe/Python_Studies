"""
Faça um programa uqe leia três números
e mostre qual é o maior e qual é
o menor.
"""
n1 = int(input('Digite um número: ').strip())
n2 = int(input('Digite outro número: ').strip())
n3 = int(input('Digite o último número: ').strip())

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

print('Menor número: {}'.format(menor))

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

print('Maior número: {}'.format(maior))
"""ou
if n1 < n2 and n1 < n3:
    print('Menor número: {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('Menor número: {}'.format(n2))
else:
    print('Menor número: {}'.format(n3))

if n1 > n2 and n1 > n3:
    print('Maior Número: {}.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('Maior número: {}'.format(n2))
else:
    print('Maior número: {}'.format(n3))

"""

