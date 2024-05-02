"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim, e passo. E realize
a contagem.

Seu programa tem que realizar três contagens através
da função criada:

A) De 1 até 10, de 1 em 1.
B) De 10 até 0, de 2 em 2.
C) Uma contagem personalizada.
"""
from time import sleep

def contador(inicio, fim, passo):
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print()
    elif fim < inicio:
        if passo > 0:
            for i in range(inicio, fim - 1, - passo):
                print(i, end=' ', flush=True)
                sleep(0.5)
            print()
        else:
            for i in range(inicio, fim, passo):
                print(i, end=' ', flush=True)
                sleep(0.5)
            print()
    
def linha():
    print('-'*60)


#Código principal
linha()
print('Contando de 1 até 10 no intervalo de 1 número.')
contador(1, 10, 1)
linha()
print('Contando de 10 até 1 no intervalo de 2 npumeros.')
contador(10, 0, 2)
linha()
print('Agora é a sua vez! Monte sua contagem personalizada.')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if p == 0:
    p = 1
linha()
print('Contagem personalizada: ')
contador(i, f, p)
linha()