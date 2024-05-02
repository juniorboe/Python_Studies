"""
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[], [], []]
somaDosPares = 0
somaTerceiraColuna = 0
maiorDaSegundaLinha = 0

for c in range(0, 3): #Início do loop da matriz
    for i in range(0, 3): #Início do loop para cada lista de #matriz
        num = int(input(f'Digite um número para [{c}, {i}]: ')) #input para adicionar os números em cada lugar da lista da matriz
        matriz[c].append(num) #Adicionando os números à matriz

        if num % 2 == 0: #Condicional para a resolução da letra A
            somaDosPares += num

        if i == 2: #Condicional para a resolução da letra B
            somaTerceiraColuna += num

        if c == 1: #Condicional para a resolução da letra C
            if i == 0:
                maiorDaSegundaLinha = num
            else:
                if num > maiorDaSegundaLinha:
                    maiorDaSegundaLinha = num
        



print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]')
print(f'A soma dos números pares da matriz é: {somaDosPares}.')
print(f'A soma dos valores da terceira coluna é: {somaTerceiraColuna}.')
print(f'O maior número da segunda linha é: {maiorDaSegundaLinha}')
