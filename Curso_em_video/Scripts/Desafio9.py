"""
Faça um programa que leia um número
inteiro qualquer e mostre na tela
a sua tabuada.
"""

num = int(input('Digite um número: '));
i = 1;

for i in range(1, 11):
    res = num * i;
    print('{} x {} = {}'.format(num, i, res));

"""i = 1;

while i <= 10:
    res = num * i;
    print('{} x {} = {}'.format(num, i, res))
    i += 1;"""