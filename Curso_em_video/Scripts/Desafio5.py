"""
Faça um programa que leia um número
inteiro e mostre na tela o seu 
sucessor e seu antecessor.
"""

num = int(input('Digite um número: '));

numA = num - 1;
numS = num + 1;

print('O antecessor do número digitado é {}, e o seu sucessor é {}.'.format(numA, numS));