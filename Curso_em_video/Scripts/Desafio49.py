"""
Refaça o desafio 009, mostrando a tabuada de
um número que o usuário escolher, só que
agora utilizando um laço for.
"""
print('\033[32mTabuada:\033[m')
n = int(input('Digite um número, e saiba a sua tabuada: '))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, n*i))

