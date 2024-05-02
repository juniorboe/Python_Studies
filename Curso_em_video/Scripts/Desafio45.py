"""
Crie um programa que faça o computador jogar 
Jokenpô(pedra, papel ou tesoura) com você.
"""
from random import randint

pedra = 1
papel = 2
tesoura = 3

print('\033[7;35mBem vindo ao jogo Jokempô!\n\033[m'
      '\033[1;35mQual é a sua jogada?\033[m\n')

jogPlayer = int(input('\033[1;35m1- Pedra.\n2- Papel.\n3-Tesoura.\n\033[m'))

while jogPlayer < 1 or jogPlayer > 3:
    print('\033[1;31mEntrada incorreta!\n\033[m')
    jogPlayer = int(input('\033[1;35m1- Pedra.\n2- Papel.\n3-Tesoura.\n\033[m'))

if jogPlayer == 1:
    escolhaPlayer = 'Pedra'
elif jogPlayer == 2:
    escolhaPlayer = 'Papel'
else:
    escolhaPlayer = 'Tesoura'

jogComp = int(randint(1, 3))

if jogComp == 1:
    escolhaComp = 'Pedra'
elif jogComp == 2:
    escolhaComp = 'Papel'
else:
    escolhaComp = 'Tesoura'

print('\033[1;35m\nPreparando jogada...\n\033[m')

if jogPlayer == jogComp:
    print('\033[1;35mPlayer: {}.\n'
          'Computador: {}.\033[m\n'
          '\033[7;35mEmpate!\033[m'.format(escolhaPlayer, escolhaComp))
elif (jogPlayer == 1 and jogComp == 3) or (jogPlayer == 2 and jogComp == 1) or (jogPlayer == 3 and jogComp == 2):
    print('\033[1;35mPlayer: {}.\n'
          'Computador: {}.\n\033[m'
          '\033[7;35mVocê ganhou!\033[m'.format(escolhaPlayer, escolhaComp))
else:
    print('\033[1;35mPlayer: {}.\n'
          'Computador: {}.\n\033[m'
          '\033[7;35mVocê perdeu!\033[m'.format(escolhaPlayer, escolhaComp))



