"""
Faça um programa que calcule a soma entre
todos os números ímpares que são múltiplos
de três e que se encontram no intervalo
de 1 até 500.
"""
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1

print('O somatório dos {} valores é: {}.'.format(cont, soma))
        
