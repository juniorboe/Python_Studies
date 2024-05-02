"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final, 
coloque esse dicionário em ordem, sabendo que o vencedor tirou o
maior número.
"""
from random import randint
from time import sleep
from operator import itemgetter

#Quatro jogadores jogam um dado e tenham resultados aleatórios
print('Sorteando as jogadas')
jogadas = []
for i in range(1, 5):
    jogada = randint(1, 6)
    print(f'O jogador {i} tirou {jogada}')
    sleep(0.5)
    jogadas.append(jogada)

#Guardar os resultados em um dicionário
jogo = {} 

jogo['Jogador 1'] = jogadas[0]
jogo['Jogador 2'] = jogadas[1]
jogo['Jogador 3'] = jogadas[2]
jogo['Jogador 4'] = jogadas[3]

#{'player1': 5, 'player2': 2, 'player3': 6, 'player4': 1}
#Colocando o dicionário em ordem crescente
print('\nRevisando os resultados...\n')
sleep(0.5)
jogo = sorted(jogo.items(), key = itemgetter(1), reverse = True)

#Printando o resultado
for pos, c in enumerate(jogo):
    print(f'O {pos + 1}º colocado é o {c[0]}. Número sorteado: {c[1]}.')


