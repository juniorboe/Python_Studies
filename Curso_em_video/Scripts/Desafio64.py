"""
Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos 
números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""

num = int(input('Digite um número: '))
soma = 0
count = 0
while num != 999:
    soma += num
    count += 1
    num = int(input('Digite outro número: '))
print('\033[1;34mNúmeros digitados: {}.\n'
      'Soma dos números digitados: {}.\033[m'.format(count, soma))