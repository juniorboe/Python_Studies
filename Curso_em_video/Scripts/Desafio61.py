"""
Refaã o DESAFIO 051, lendo o primeiro termo e a 
razão de uma PA, mostrando os 10 primeiros termos da 
progressão usando a estrutura while.
"""

#fórmula da PA: ultimo = primeiro + (n - 1) * razao

#variáveis
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
count = 1

#loop de cálculo
while count <= 10:
    print('{} - '.format(termo), end=' ')
    termo += razao
    count += 1
print('Acabou!')
