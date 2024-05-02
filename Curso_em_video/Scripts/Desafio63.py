"""
Escreva um programa que leia um número
n inteiro qualquer
-------
e mostre na tela os n
primeiros elementos de uma Sequência de 
Fibonacci

A sucessão de Fibonacci é uma sequência de 
números inteiros iniciados por zero e um,
no qual cada termo subsequente corresponde a soma
dos dois números anteriores: 0, 1, 1, 2, 3, 5, 8
"""
#variáveis
count = int(input('Digite quantos elementos você quer mostrar na sequência de Fibonacci: '))
a = 0
b = 1
#algoritmo
print('{}, {}'.format(a, b), end=', ')
while (count - 2) > 0:
    fib = a + b #1 2 3 5
    print('{}'.format(fib), end=', ')
    a = b #1 1 2 3
    b = fib #1 2 3 5
    count -= 1
print('Acabou')
