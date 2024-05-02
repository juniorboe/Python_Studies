"""
Crie um programa que leia o nome de uma
pessoa e diga se ela tem 'Silva' no nome
"""

nome = str(input('Digite seu nome completo: '));

if("silva" in nome.lower()):
    print('O nome contém "Silva".');
else:
    print('O nome não contém "Silva".');