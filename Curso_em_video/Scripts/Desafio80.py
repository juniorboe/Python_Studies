"""
Crie um programa onde o usuário possa digitar cinco
valores numéricos, e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""

lista = []
for i in range(0, 5):
    num = int(input('Digite um número: '))

    if i == 0 or num > lista[-1]:
        lista.append(num)
        print('O número digitado assumiu o final da lista.')
    else:
        for pos, c in enumerate(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'O número digitado assumiu a posição {pos + 1} da lista.')
                break
print(lista)