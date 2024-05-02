"""
Variáveis compostas (Quase o mesmo que array list)

- Tuplas usam ()
- Tuplas são imutáveis
Forma de inicializar uma tupla:
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

Formas de iterar sobre tuplas:

for comida in lanche:
    print(f'Eu vou comer {comida}')

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]} na posição {i}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

- print(sorted(lanche)) -> Ordena em ordem alfabética

--------------------------------------------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b -> (2, 5, 4, 5, 8, 1, 2) #O sinal de + irá concatenar as tuplas

- É possível utilizar métodos internos nas tuplas. Ex: .count(), .index(), entre outros

-----------------------------------------------------------------------------------------

- Tuplas aceitam mais de um tipo de variável
- Pode-se apagar uma tupla utilizando del(#nome_da_tupla)
"""