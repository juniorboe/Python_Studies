"""
Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o 
menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar
valores.
"""

#variáveis
num = int(input('Digite um número inteiro: '))
maior = num
menor = num
count = 1
soma = num
#algoritmo
res = str(input('Você quer seguir digitando valores? (S/N) ')).upper().strip()
while res == 'S':
    num = int(input('Digite um número inteiro: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    count += 1
    res = str(input('Você quer seguir digitando valores? (S/N) ')).upper().strip()
media = soma / count
print('~'*30)
print('O maior número é: {}.\n'
      'O menor número é: {}.\n'
      'A média dos números digitados é: {:.2f}.'.format(maior, menor, media))
print('~'*30)
