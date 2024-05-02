"""
Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos 
números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""
#inicializando variáveis
num = soma = count = 0
#loop infinito de repetição, usando o break como parada após uma condição
while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        print('Flag!')
        break
    soma += num
    count += 1
print('-'*30)
print(f'A soma dos {count} valores foi {soma}.')
