"""
Faça um programa que leia o nome
completo de uma pessoa, mostrando em 
seguida o primeiro nome e o 
último nome separadamente.

Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

nome = str(input('Digite seu nome completo: ')).strip()

nomeLis = nome.split()

print('Primeiro nome: {}'.format(nomeLis[0]));
print('Último nome: {}'.format(nomeLis[len(nomeLis) - 1]))
