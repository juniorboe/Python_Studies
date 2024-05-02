"""
Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO
"""
from datetime import date

ano = int(input('Que ano você quer analisar?\n'
                'Digite 0 caso queira analisar o ano atual. ').strip())

if ano == 0:
    ano = date.today().year

if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
    print('{} é ano bissexto!'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))