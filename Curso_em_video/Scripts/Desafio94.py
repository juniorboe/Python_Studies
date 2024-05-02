"""
Crie um programa que leia o nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
"""
#Lendo o nome, sexo e idade de várias pessoas, e guardando em um dicionário
grupo = []
while True:
    pessoa = dict()

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()

    pessoa['Nome'] = nome
    pessoa['Idade'] = idade
    pessoa['Sexo'] = sexo
    grupo.append(pessoa)

    continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input('Erro de digitação. Deseja continuar[S/N]? ')).strip().upper()
    if continuar == "N":
        break      

print('-='*30)
#Mostrando quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(grupo)} pessoas.')

#Mostrando a média de idade do grupo
somaIdade = 0
for pos, c in enumerate(grupo):
    somaIdade += grupo[pos]['Idade']
mediaIdade = somaIdade / len(grupo)
print(f'A média de idade do grupo é: {mediaIdade:.2f}')

#Mostrando a lista com todas as mulheres
mulheres = []
for pos, c in enumerate(grupo):
    if grupo[pos]['Sexo'] == "F":
        mulheres.append(c['Nome'])
print(f'As mulheres do grupo são: ', end='')
for c in mulheres:
    print(c, end='. ')
print('')

#Mostrando lista de todas as pessoas com idade acima da média
acimaDaMedia = []
for pos, c in enumerate(grupo):
    if grupo[pos]['Idade'] > mediaIdade:
        acimaDaMedia.append(c['Nome'])
print(f'Pessoas com idade acima da média: ', end='')
for c in acimaDaMedia:
    print(f'{c}', end='. ')
