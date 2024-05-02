"""
Crie um programa que leia o nome
de uma cidade e diga se ela começa
com o nome 'Santo'
"""

cidade = str(input('Digite o nome de uma cidade: ')).strip();

cidadeLis = cidade.upper().split();

if("SANTO" in cidadeLis[0]):
    print('{} contém "Santo" no início.'.format(cidade));
else:
    print('{} não contém "Santo" no início.'.format(cidade));