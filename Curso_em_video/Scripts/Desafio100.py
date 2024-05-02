"""
Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista,
e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterios.
"""
from random import randint
from time import sleep

def sorteia():  
    for i in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
    print('Sorteando os valores', end=': ')
    for i in numeros:
        print(i, end=' ', flush=True)
        sleep(0.5)
    print()
    print(f'Lista com números aleatórios: {numeros}')

def somaPar(lst):
    soma = 0
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos números pares é: {soma}.')


#Código principal
numeros = list()
sorteia()
somaPar(numeros)
