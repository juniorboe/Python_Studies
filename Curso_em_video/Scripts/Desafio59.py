"""
Crie um programa que leia dois valores e 
mostre um menu na tela: 

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso.
"""

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print('Primeiro número = {}\n Segundo número = {}.\n'.format(num1, num2))
menu = int(input('Digite abaixo, conforme os números do índice do menu, o que você deseja fazer com os números digitados:\n'
                 '[1] Somar.\n'
                 '[2] Multiplicar.\n'
                 '[3] Maior.\n'
                 '[4] Novos números.\n'
                 '[5] Sair do programa.\n'))

while menu < 1 or menu > 5:
    menu = int(input('\033[31mErro de digitação!\n\033[mDigite abaixo, conforme os números do índice do menu, o que você deseja fazer com os números digitados:\n'
                 '[1] Somar.\n'
                 '[2] Multiplicar.\n'
                 '[3] Maior.\n'
                 '[4] Novos números.\n'
                 '[5] Sair do programa.\n'))

while menu != 5:
    if menu == 1:
        soma = num1 + num2
        print('A soma dos números é: {}.\n'.format(soma))
    elif menu == 2:
        mult = num1 * num2
        print('A multiplicação dos números é: {:.2f}\n.'.format(mult))
    elif menu == 3:
        if num1 > num2:
            maiorNum = num1
            print('O maior número é: {}.\n'.format(num1))
        elif num1 < num2:
            maiorNum = num2
            print('O maior número é: {}.\n'.format(num2))
        else:
            print('Os dois números são iguais!\n')
    elif menu == 4:
        print('Digite novamente os números.')
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro número: '))
        print('Os novos números são: {} e {}.\n'.format(num1, num2))
    menu = int(input('Digite abaixo, conforme os números do índice do menu, o que você deseja fazer com os números digitados:\n'
                 '[1] Somar.\n'
                 '[2] Multiplicar.\n'
                 '[3] Maior.\n'
                 '[4] Novos números.\n'
                 '[5] Sair do programa.\n'))
print('Saindo do programa...')
