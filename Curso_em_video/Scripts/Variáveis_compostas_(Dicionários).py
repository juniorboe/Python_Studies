"""
Dicionários é um tipo de variável composta que permite usar nomes literais
ao invés de índices.

Para declarar um dicionário, precisa usar o comando #dict(), ou #{}.
Ex: 
    dados = dict()
    ou
    dados = {}

Ex. 2:
    dados = {'nome': 'Pedro', 'idade': 25}

----------------------------------------------------------------------------

O Python reconhece o dicionário da seguinte forma:

dados = {'nome': 'Pedro', 'idade': 25}

print(dados.values()) => #dict_values([Pedro, 25)] => values(), ou valores, são o conteúdo
do dicionário.

print(dados.keys()) => #dict_keys(['nome', 'idade']) => keys(), ou chaves, são os nomes
literais dados às variáveis declarada em um dicionário.

print(dados.items()) => #dict_items{[('nome', 'Pedro'), ('idade', 25)]} => items(), ou itens,
são o conjunto inteiro de dados do dicionário, incluindo keys e values.

----------------------------------------------------------------------------

Exemplo de exibição de valores armazenadas em um dicionário:

dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome']) => #Pedro
print(dados['idade']) => 25

----------------------------------------------------------------------------

Para adicionar itens em um dicionário, não utiliza-se o .append(), só é
necessário declarar um item novo dentro da estrutura do dicionário.
Ex:

dados = {'nome': 'Pedro', 'idade': 25}
dados['sexo'] = 'M' => #dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}

----------------------------------------------------------------------------

Para excluir um item, usa-se o comando #del.
Ex:

dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
del dados['idade'] => #dados = {'nome': 'Pedro', 'sexo': 'M'}

----------------------------------------------------------------------------

Para modificar um valor em dicionários, é preciso apenas declarar o mesmo
utilizando a key a ser declarada.
Ex:

dados = {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
dados['nome'] = 'João'
print(dados.items()) => dict_items{[('nome', 'João'), ('idade', 25), ('sexo', 'M')]} 

----------------------------------------------------------------------------

Laço de repetição utilizando keys e values.
Ex:

filme = {'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
        }

Para laços utilizando .items(), é necessário ter duas variáveis de controle,
a primeira para #keys, e a segunda para #values.
Ex:
for k, v in filme.items():
    print(f'O (k) é (v)')

    #O titulo é Star Wars
    #O ano é 1977
    #O diretor é George Lucas        

Para iterar sobre .keys(), ou .values(), é necessário apenas uma variável
de controle.
Ex:
for k in filme.keys():
    print(k)
    
    #titulo
    #ano
    #diretor

ou

for v in filme.values():
    print(v)
    #Star Wars
    #1977
    #George Lucas
----------------------------------------------------------------------------

É permitido armazenar dicionários em listas, e fazer operações de listas
normalmente.
Ex:
filme1 = {'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
        }

filme2 = {'titulo': 'Avangers',
        'ano': 2012,
        'diretor': 'Joss Whedon'
        }

filme3 = {'titulo': 'Matrix',
        'ano': 1999,
        'diretor': 'Wachowski'
        }

locadora = list()

locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)

print(locadora)
    #[{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'},
    {'titulo': 'Avangers', 'ano': 2012, 'diretor': 'Joss Whedon'},
    {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'}]

print(locadora[0]['ano']) => #1977
print(locadora[2]['titulo']) => #Matrix

----------------------------------------------------------------------------

Para criar dicionários dentro de listas usando inputs com iterações:
estado = {} #Inicializando o dicionário para adicionar em uma lista
brasil = [] #Inicializando a lista

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #O .copy() tem o mesmo efeito da cópia
        utilizando fatiamento #[:] usada em listas.
    
    #uf e siglas digitadas = Rio Grande do Sul, RS, Santa Catarina, SC, Paraná, PR
    for e in brasil:
        print(e)
        #{'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
        #{'uf': 'Santa Catarina', 'sigla': 'SC'}
        #{'uf': 'Paraná', 'sigla': 'PR'}

    ou

    for e in brasil:
        for v in e.values():
        #Rio Grande do Sul
        #RS
        #Santa Catarina   
        #SC
        #Paraná
        #PR
    
    ou

    for e in brasil:
        for k, v in e.items():
            print({k} tem valor {v})
            
            #uf tem valor Rio Grande do Sul
            #sigla tem valor RS
            #uf tem valor Santa Catarina   
            #sigla tem valor SC
            #uf tem valor Paraná
            #sigla tem valor PR

----------------------------------------------------------------------------

Para ordenar um dicionário, é necessário usar o método #sorted, usando 
como parâmetro o #item() do dicionário a ser ordenado, juntamente com uma 
key, que utiliza a função #itemgetter da biblioteca #operator.

from operator import itemgetter

jogadas = {'Jogador 1': 3, 'Jogador 2': 7, 'Jogador 3': 2, 'Jogador 4': 6}
jogadasOrdenadas = {}
jogadasOrdenadas = sorted(jogadas.item(), key=itemgetter(1), reverse=True)
print(jogadasOrdenadas)
# [('Jogador 2', 7), ('Jogador 4', 6), ('Jogador 1', 3), ('Jogador 3', 2)]

Observações:
    #O valor dentro dos parênteses de #itemgetter serve para pegar o
    índice a ser utilizado na ordenação. No caso do exemplo acima, o
    índice 1 é o #value do dicionário. Se utilizasse 0, seria a #key.

    #O método #sorted() retorna uma LISTA, e não um dicionário. Portanto,
    os métodos de tratamento dos dados posteriores ao #sorted, deverão
    ser baseados em listas, e não em dicionários. A menos que se converta
    posteriormente, a lista em um dicionário.

    #No exemplo acima, foi utilizado o método #reverse=True para mudar
    a ordem da ordenação do dicionário. Pois o método #sorted() posiciona
    a lista em ordem crescente.

"""