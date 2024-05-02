"""
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista.

Caso o número já exista 
lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente.
"""
from time import sleep
lista = [] #criação da lista vazia
while True: #inicialização do loop infinito
    num = int(input('Digite um número: ')) #input de valor a ser adicionado na lista

    if num in lista: #condicional para adicionar ou não o valor na lista
        print('Valor já adicionado anteriormente. Portanto, será desconsiderado.')
    else:
        lista.append(num)

    confirma = str(input('Quer continuar? [S/N] ')).strip().upper() #mensagem de confirmação da continuação do loop
    while confirma != "S" and confirma != "N":
        confirma = str(input('Erro na digitação! Quer continuar? [S/N] ')).strip().upper()
    if confirma == "N": #break do loop infinito
        print('Fechando a lista...')
        sleep(1)
        break
lista.sort() #ordenando a lista em ordem crescente
print('Valores: ', end='') #mensagem final
for c in lista:
    print(f'{c}', end='. ')
