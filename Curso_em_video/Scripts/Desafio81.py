"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []

while True: #loop infinito utilizado para a obtenção dos números da lista, até que o usuário queira parar de adicionar números.
    lista.append(int(input('Digite um número: '))) #input de inserção dos números na lista
    confirma = str(input('Quer continuar? [S/N]')).strip().upper() #prineira confirmação para continunar a adicionar números na lista
    while confirma != "S" and confirma != "N": #captação de erro de digitação na confirmação
        confirma = str(input('Resposta inválida! Quer continuar? [S/N]')).strip().upper()
    if confirma == "N": #condição de parada do loop infinito, caso a pessoa digite "N"
        print('Lista fechada.')
        break


print(f'Foram digitados {len(lista)} números.') #Resposta da letra A

lista.sort(reverse = True) #Resposta da letra B
print(f'Lista na ordem decrescente:',end=' ')
for i in lista:
    print(i, end='. ')

for i in lista: #Resposta da letra C
    if i == 5:
        print(f'\nO valor 5 foi digitado, e está na posição {lista.index(5) + 1} da lista.')
    else:
        print('O valor 5 não foi encontrado na lista.')
