"""
Faça um programa que jogue par ou 
ímpar com o computador. O jogo só será
interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
"""
from random import randint
from time import sleep

vitorias = 0

while True:
    #inicializando variáveis
    escolha = str(input('Você escolhe par, ou ímpar?\n')).strip().upper()
    #captando erro da variavel {escolha}
    while escolha != "PAR" and escolha != "IMPAR" and escolha != "ÍMPAR":
        print('\033[1;31m\nOpção inválida!\033[m')
        escolha = str(input('Você escolhe par, ou ímpar?\n')).strip().upper()
    jogComp = int(randint(1, 2))
    jogPlayer = int(input('Escolha um número: \n'))
    resultado = jogComp + jogPlayer


    #Algoritmo do resultado do jogo, utilizando condicionais
    if escolha == "PAR" and resultado % 2 == 0:
        print('-='*20)
        print('Calculando jogada...\n')
        sleep(1)
        print('Você ganhou!')
        print(f'Sua jogada: {jogPlayer}.\nJogada do computador: {jogComp}.\nResultado: {resultado}.')
        print('-='*20)
        print('\nJogando novamente...')
        sleep(0.5)
        vitorias += 1
    elif (escolha == "ÍMPAR" or escolha == "IMPAR") and resultado % 2 != 0:
        print('-='*20)
        print('Calculando jogada...\n')
        sleep(1)
        print('Você ganhou!')
        print(f'Sua jogada: {jogPlayer}.\nJogada do computador: {jogComp}.\nResultado: {resultado}.')
        print('-='*20)
        print('\nJogando novamente...')
        sleep(0.5)
        vitorias += 1
    else:
        print('-='*20)
        print('Calculando jogada...\n')
        sleep(1)
        print('Você perdeu.')
        print(f'Sua jogada: {jogPlayer}.\nJogada do computador: {jogComp}.\nResultado: {resultado}.')
        print('-='*20)
        break
print(f'\033[1;34mO número de vitórias consecutivas atingido foi: {vitorias}.\033[m')
