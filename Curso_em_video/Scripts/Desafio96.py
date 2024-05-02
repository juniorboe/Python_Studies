"""
Faça um programa que tenha uma função chamada area(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre
a área do terreno.
"""
def area(l, c):
    a = l * c
    print(f'A área do seu terreno de {c}x{l}m é de {a}m².')


print(f'{'Controle de terrenos':^25}')
print('-'*25)
c = float(input('Comprimento(m): '))
l = float(input('Largura(m): '))
area(c, l)
