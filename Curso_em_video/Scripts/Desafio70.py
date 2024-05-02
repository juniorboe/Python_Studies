"""
Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário
vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000,00.
c) Qual é o nome do produto mais barato.
"""

gasto = 0
countProdMil = 0
precoMaisBaixo = 9999999

while True:
    print('-'*40)
    #cadastrando produtos
    nome = str(input('Qual é o nome do produto: ')).strip()
    preco = float(input('Qual é o preço do produto: '))

    #análise de dados
    #somando o gasto total
    gasto += preco
    #analisando quantos produtos custam mais de 1000 reais
    if preco > 1000:
        countProdMil += 1
    #analisando o produto mais barato
    if preco < precoMaisBaixo:
        precoMaisBaixo = preco
        prodMaisBarato = nome

    #confirmação de continuação
    continuar = str(input('\nQuer continuar? [S/N] ')).strip().upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input('Quer cointinuar? [S/N] ')).strip().upper()
    #confirmação do término do programa
    if continuar == "N":
        break
print('-'*40)
print('Fim da compra')
print('-'*40)
print(f'Total gasto na compra: R${gasto:.2f}.')
print(f'{countProdMil} produtos custam mais de R$1000,00.')
print(f'O produto mais barato é: {prodMaisBarato}. Custo: R${precoMaisBaixo:.2f}')