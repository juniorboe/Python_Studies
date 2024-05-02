"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 npumeros entre 1 e 60 para cada jogo, cadastrando tudo em uma
lista composta.
"""
from random import randint
from time import sleep

palpites = []
palpite = []
print('-'*60)
print('{:^60}'.format('CRIADOR DE PALPITES DA MEGA SENA'))
print('-'*60)
numPalpites = int(input('Quantos palpites você quer gerar? '))
print(f'Você pediu {numPalpites} palpites para o sorteio da MEGA SENA.')
if numPalpites > 0:
    print('-='*10, f'Sorteando {numPalpites} palpites', '-='*10)
    for c in range(0, numPalpites):
        for i in range(0, 6):
            num = randint(1, 60)
            while True:
                if num not in palpite:
                    palpite.append(num)
                    break
                else:
                    numReserva = randint(1, 60)
                    palpite.append(numReserva)
                    break
        palpite.sort()
        palpites.append(palpite[:])
        palpite.clear()
        sleep(0.5)
        print(f'{c + 1}º palpite: {palpites[c]}')
    print('-='*12, f' Boa sorte! ', '-='*12)

else:
    print('Nenhum palpite foi gerado.')



