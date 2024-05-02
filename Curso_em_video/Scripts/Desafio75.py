"""
Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite outro valor: '))
num4 = int(input('Digite o último valor: '))

lista = (num1, num2, num3, num4)
    
print(lista)
print(f'O valor 9 apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O número 3 aparece na {lista.index(3) + 1}ª posição.')
else:
    print('A lista não contem o número 3.')

par = 0 #variável de sinalização para número par na lista. Se 0, não tem número par. Se 1, têm número par.
for i in lista: #Iteração na lista para achar algum número par.
    if i % 2 == 0:
        par = 1

if par == 0: #Se não houver número par na lista, o print abaixo será mostrado na tela
    print('A lista não tem valores pares.')
else: #Se tiver número par, o script abaixo será rodado para mostrar os números pares.
    print(f'Os valores pares são:', end=' ')
    for i in lista:
        if i % 2 == 0:
            print(i, end=' ')
