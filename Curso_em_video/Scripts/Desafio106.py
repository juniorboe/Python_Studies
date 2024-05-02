"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará

OBS: use cores.
"""
from time import sleep
cor = {0: '\033[m',         #Sem cores
       1: '\033[0;30;41m',  #Vermelhor
       2: '\033[0;30;42m',  #Verde
       3: '\033[0;30;43m',  #Amarelo
       4: '\033[0;30;44m',  #Azul
       5: '\033[0;30;45m',  #Roxo
       6: '\033[7;30m',     #Branco
       }

def mensagem(msg, c=0):
    tam = len(msg) + 4
    print(cor[c], end='')
    print('~'*tam)
    print(' ', msg, ' ')
    print('~'*tam)
    print(cor[0])


def iHelp(c):
    return help(c)


#Programa principal
mensagem('Bem vindo ao PyHelper', 2)
while True:
    prompt = str(input('Digite o comando: ')).strip()
    if prompt.upper() == 'FIM':
        mensagem('Fechando o programa...', 1)
        sleep(1)
        break

    mensagem(f'Acessando o manual do comando \'{prompt}\'', 4)
    sleep(1)

    iHelp(prompt)


