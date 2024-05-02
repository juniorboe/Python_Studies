"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[], [], []]

for c in range(0, 3):
    for i in range(0, 3):
        num = int(input(f'Digite um número para [{c}, {i}]: '))
        matriz[c].append(num)

print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]')