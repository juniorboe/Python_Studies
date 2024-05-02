"""
Listas (array list)

- É inicializada com []
- Listas podem ser mutáveis:
    Pode adicionar, excluir, e modificar variáveis.

------------------------------------------------------------------------

lanche = ['Hamburguer', 'Suco', 'Pizza', 'Sorvete']
Selecionar variável:
lanche[3] => 'Sorvete'

------------------------------------------------------------------------

Modificar variável:
lanche[2] = 'Água' => Modificará o índice 2 para #água#.
#lanche = ['Hamburguer', 'Suco', 'Água', 'Sorvete']

------------------------------------------------------------------------

Adicionar variável:
lanche.append('Cookie') => Adicionará #cookie# no final da lista.
#lanche = ['Hamburguer', 'Suco', 'Pizza', 'Sorvete', 'Cookie']

lanche.insert(0, 'Cachorro quente') => Adicionará #Cachorro quente# no índice 0 da lista.
#lanche = ['Cachorro quente', 'Hamburguer', 'Suco', 'Pizza', 'Sorvete', 'Cookie']

------------------------------------------------------------------------

Remover variável:
del lanche[3] => Removerá o índice 3 da lista.
#lanche = ['Cachorro quente', 'Hamburguer', 'Suco', 'Sorvete', 'Cookie']

lanche.pop(3) => Removerá o índice 3 da lista. (o método pop() sem parâmetro remove o último índice da lista)
#lanche = ['Cachorro quente', 'Hamburguer', 'Suco', 'Sorvete', 'Cookie']

lanche.remove('Pizza') => Remove o índice com o valor 'Pizza'.
#lanche = ['Cachorro quente', 'Hamburguer', 'Suco', 'Sorvete', 'Cookie']

------------------------------------------------------------------------

Para criar uma lista ordenada:
Usar a função list(range())
valores = list(range(4, 11)) => Retornará uma lista de seis elementos, com valores de 4 até 10.
#valores = [4, 5, 6, 7, 8, 9, 10]

------------------------------------------------------------------------

Para listas não ordenadas:
Criar 'a mão':
#valores = [8, 2, 5, 4, 9, 3, 0]

------------------------------------------------------------------------

Para ordenar uma lista:
valores.sort() => Ordena em ordem crescente.
#valores = [0, 2, 3, 4, 5, 8, 9]
valores.sort(reverse = True) => Ordena em ordem decrescente.
#valores = [9, 8, 5, 4, 3, 2, 0]

------------------------------------------------------------------------

Para saber o tamanho da lista:
len(valores) => Retorna quantos elementos tem a lista.
#7

------------------------------------------------------------------------

a = [2, 3, 4, 7]
b = a => Cria uma cópia da a com ligação entre as duas listas
#b = [2, 3, 4, 7]
Se mudar um valor de #b#, mudará o mesmo valor em #a#
b[2] = 8
print(a) => Retornará #[2, 3, 8, 7]
print(b) => Retornará #[2, 3, 8, 7]

b = a[:] => Utilizando fatiamento, criará uma cópia sem criar ligação entre as listas
#b = [2, 3, 4, 7]
Se mudar um valor de #b#, não mudará nada em #a#
b[2] = 8
print(a) => Retornará #[2, 3, 4, 7]
print(b) => Retornará #[2, 3, 8, 7] 

-------------------------------------------------------------------------------------------------

Listas podem ser aplicadas dentro de uma outra lista
ex:
dados = ['Pedro', 25]
dados2 = ['João', 21]
dados3 = ['Maria', 32]

pessoas = list()
pessoas.append(dados[:]) #Este comando incluirá #dados# dentro da lista #pessoas#
pessoas.append(dados2[:])
pessoas.append(dados3[:])
print(pessoas) => Retornará # [['Pedro', 25], ['João', 21], ['Maria', 32]]

--------------------------------------------------------------------------------------------------

Para selecionar uma variável de uma lista, pode usar o seletor de listas com o índice a ser selecionado, com a utilização da ordem decrescente.
ex:

print(pessoas[0][0]) => Retornará #Pedro
print(pessoas[1][1]) => Retornará #21
print(pessoas[2][0]) => Retornará #Maria
print(pessoas[1]) => Retornará #['João', 21]

--------------------------------------------------------------------------------------------------

Para criar uma outra lista em cima da mesma existente, precisa usar o fatiamento, para não criar ligação entre as listas
teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:]) #Se não usar o fatiamento #[:], uma lista irá conectar na outra
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

----------------------------------------------------------------------------------------------------

Para fazer uma lista utilizando inputs:

galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int('Idade: '))
    galera.append(dado[:]) #Importante colocar #[:] para não criar ligação entre as listas.
    dado.clear() #Se não criar uma cópia #[:] no comando acima, o clear() irá limpar todas as listas de #galera, pois todas as listas estarão ligadas entre si.
print(galera) => Retornará três listas com ['nome', idade] digitados no input

"""