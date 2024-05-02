"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
"""
from time import sleep

def maior(*num):
    maior = 0
    print('Analisando valores...')
    sleep(1)
    for i in num:
        if i == num[0]:
            maior = i
        else:
            if maior < i:
                maior = i
    print(f'Valores: {num}')
    print(f'Quantidade de valores passados: {len(num)}.')
    print(f'O maior número da lista é: {maior}.')
    sleep(0.5)


#Código principal
"""numeros = list()
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input('Erro na digitação. Deseja continuar [S/N]? ')).strip().upper()
    if continuar == "N":
        break

print(numeros)"""
maior(2, 3, 7, 4, 1)
maior(3, 6, 1)