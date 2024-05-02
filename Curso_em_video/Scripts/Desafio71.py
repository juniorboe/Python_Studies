"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédilas de cada
valor serão entregues.

Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
print('='*50)
print('{:^50}'.format('Bem vindo ao Banco X'))
print('='*50)

valor = int(input('Qual é o valor que você quer sacar? R$'))
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0
while True:
    if valor >= 50:
        valor -= 50
        ced50 += 1
    elif valor < 50 and valor >= 20:
        valor -= 20
        ced20 += 1
    elif valor < 20 and valor >= 10:
        valor -= 10
        ced10 += 1
    elif valor < 10 and valor >= 1:
        valor -= 1
        ced1 += 1
    else:
        break
print(f'Total de {ced50} cédulas de R$50.\nTotal de {ced20} cédulas de R$20.\nTotal de {ced10} cédulas de R$10.\nTotal de {ced1} cédulas de R$1.')
print('='*50)
print('Volte sempre ao BANCO X! Tenha um bom dia!')
