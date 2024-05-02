"""
Escreva um progtrama que faça o
computador 'pensar' em um número
inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi
o número escolhido pelo computador

O programa deverá escrever na tela
se o usuário venceu ou perdeu.
"""
from random import randint

print('Gerando um número de 1 a 5...')
n = int(randint(1, 5))

print('-' * 30)

escolha = int(input('Tente descobrir o número escolhido pelo computador: ').strip())
while escolha < 1 or escolha > 5:
    escolha = int(input('Número inválido, tente novamente: ').strip())

if n == escolha:
    print('Número: {}.\nEscolha: {}.\nParabéns, Você acertou!'.format(n, escolha))
else:
    print('Número: {}.\nEscolha: {}.\nQue pena, não foi dessa vez...'.format(n, escolha))
