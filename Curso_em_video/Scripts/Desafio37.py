"""
Escreva um programa que leia um número
inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:

1- Binário
2- Octal
3- Hexadecimal
"""

num = int(input('Digite um número inteiro: ').strip())

conversao = str(input('Digite conforme os números abaixo, qual é a conversão que você deseja fazer.\n'
                      '1- Binário.\n2- Octal.\n3- Hexadecimal.\n').strip())

while conversao != '1' and conversao != '2' and conversao != '3':
    conversao = str(input('Digite conforme os números abaixo, qual é a conversão que você deseja fazer.\n'
                      '1- Binário.\n2- Octal.\n3- Hexadecimal.\n').strip())

if conversao == '1':
    print('{} em binário é: {}'.format(num, bin(num)))
elif conversao == '2':
    print('{} em octal é: {}'.format(num, oct(num)))
elif conversao == '3':
    print('{} em hexadecimal é: {}.'.format(num, hex(num)))

