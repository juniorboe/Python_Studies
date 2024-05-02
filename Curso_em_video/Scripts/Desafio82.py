"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

listaPrincipal = []
listaPar = []
listaImpar = []

while True: #loop infinito para a captação dos elementos da lista
    num = int(input('Digite um número: ')) #input de captação dos números da lista
    if num in listaPrincipal:
        print(f'O número {num} já existe na lista!')
        continua = str(input('Quer continuar? [S/N] ')).strip().upper() #input de confirmação para continuar a incluir elementos na lista
    else:
        listaPrincipal.append(num)
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continua != "S" and continua != "N": #loop de erro na digitação da confirmação de continuação
        continua = str(input('Resposta inválida! Quer continuar? [S/N] ')).strip().upper()
    if continua == "N": #condição de parada do loop, caso a pessoa digite "N"
        print('Lista principal fechada.')
        break

for i in listaPrincipal: #laço de detecção dos números pares e ímpares
    if i % 2 == 0: #condição dos números par
        listaPar.append(i)
    else: #condição dos números ímpares
        listaImpar.append(i)

print('-='*40)
print(f'Lista: {listaPrincipal}') #print da lista principal
print(f'Numeros pares da lista: {listaPar}') #print da lista com números pares
print(f'Números ímpares da lista: {listaImpar}') #print da lista com números ímpares