"""
Refaça o desafio 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais.
- Isósceles: Dois lados iguais.
- Escaleno: Todos os lados diferentes.
"""

l1 = float(input('Digite o comprimento do lado 1: ').strip())
l2 = float(input('Digite o comprimento do lado 2: ').strip())
l3 = float(input('Digite o comprimento do lado 3: ').strip())

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('\033[1;32mPode formar um triângulo!\033[m\nTipo de triängulo: Equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('\033[1;32mPode formar um triângulo!\033[m\nTipo de triângulo: Isósceles.')
    else:
        print('\033[1;32mPode formar um triângulo!\033[m\nTipo de triângulo: Escaleno.')
else:
    print('\033[1;31mNão pode ser um triângulo!\033[m')
