"""
Desenvolva um programa que leia o primeiro
termo e a razão de uma Progressão
Aritmética. No final, mostre os 10 primeiros
termos dessa progressão.
"""

primeiro = int(input('Digite o primeiro termo: ').strip())
razao = int(input('Digite a razão: ').strip())
n = 10
ultimo = primeiro + (n - 1) * razao

for i in range(primeiro, ultimo + 1, razao):
    print(i, end = ' ')
print('Acabou')