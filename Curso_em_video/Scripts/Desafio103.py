"""
Faça um programa que tenha  uma função chamada ficha(), que receba dois parâmetros
opcionais: o NOME de um jogador e quantos GOLS ele marcou.

O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado
não tenha sido informado corretamente.
"""

def ficha(jog='<desconhecido>', gls=0):
    return f'O jogador {jog} fez {gls} gols.'
    

#Programa principal    
jogador = str(input('Nome do jogador: ')).strip()
qtdGols = str(input('Quantos gols o jogador fez? '))
if qtdGols.isnumeric():
    qtdGols = int(qtdGols)
else:
    qtdGols = 0
if jogador == '':
    print(ficha(gls=qtdGols))
else:
    print(ficha(jogador, qtdGols))
