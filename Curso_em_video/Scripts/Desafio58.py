"""
Melhore o jogo do DESAFIO 028 onde o 
computador vai 'pensar' em um número entre
0 e 10. Só que agora o jogador vai tentar
advinhar até acertar, mostrando no final 
quantos palpites foram necessários para
vencer.
"""

from random import randint
import time
contadorPalpites = 1
print('Gerando um número de 1 a 10...')
n = int(randint(1, 10))
time.sleep(1)
print('-' * 30)
print('Sua vez!, tente acertar o número escolhido pelo computador.')

escolha = int(input('Escolha: '))
while escolha < 1 and escolha > 10:
    print('\033[31mERRO! Número fora do range de 1 a 10.\033[m')
    escolha = int(input('Escolha: '))

while escolha != n:
    escolha = int(input('Errou! Tente novamente: '))
    contadorPalpites += 1
print('Você acertou! O número escolhido é: {}\n'
      'Nº de palpites: {}.'.format(escolha, contadorPalpites))
