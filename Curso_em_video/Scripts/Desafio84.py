"""
Faça um programa que leia o nome e peso de várias pessoas, guardando 
tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas. (Se houver mais de uma pessoa com o mesmo peso, mostrar todas as pessoas com este peso)
C) Uma listagem com as pessoas mais leves. (Se houver mais de uma pessoa com o mesmo peso, mostrar todas as pessoas com este peso)
"""
pessoas = list()
dados = list()

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    while continuar != "S" and continuar != "N":
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == "N":
        break


maiorPeso = 0
maisPesados = list()
menorPeso = 0
menosPesados = list()
for pos, c in enumerate(pessoas):
    if pos == 0: #Condicional para iniciar as listas #maisPesados e #menosPesados, e as variáveis de controle #maiorPeso e #menorPeso
        maiorPeso = c[1]
        maisPesados.append(c[0])
        menorPeso = c[1]
        menosPesados.append(c[0])
        
    else: #condicional para analisar os itens restantes da lista
        if c[1] > maiorPeso: #Se o peso analisado for maior que o maior peso atual, ele assume o #maiorPeso e adiciona a pessoa na lista de #maisPesados
            maiorPeso = c[1]
            del maisPesados[:] #comando para zerar a lista, e deixá-la disponível para adicionar o #maisPesados
            maisPesados.append(c[0]) #Adicionando o #maisPesado
            
        elif c[1] == maiorPeso: #Caso o #maiorPeso for igual ao atual, apenas adicionará mais uma pessoa em #maisPesados
            maisPesados.append(c[0])
            
        elif c[1] < menorPeso: #Se o peso analisado for menor que o #menosPesado atual, ele assume o #menorPeso
            menorPeso = c[1]
            del menosPesados[:] #Comando para limpar o #menosPesados para adicionar o novo menos pesado
            menosPesados.append(c[0])
            
        elif c[1] == menorPeso: #Se o peso analisado for igual ao #menorPeso, apenas adicionará o nome da pessoa ao #menosPesados
            menosPesados.append(c[0])
            

print(f'O número de pessoas cadastradas é: {len(pessoas)}.') #Resultado da letra A.
print(f'O maior peso foi {maiorPeso}. Pessoa(s) com o maior peso: {maisPesados}')
print(f'O menor peso foi {menorPeso}. Pessoa(s) com o menor peso: {menosPesados}')