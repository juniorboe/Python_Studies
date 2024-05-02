"""
Crie uma tupla preenchida com os 20 primeiros
colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time do Internacional.
"""

tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Lista de times do Brasileirão: {tabela}')
print('-'*50)
print(f'Os cinco primeiros são {tabela[:5]}')
print('-'*50)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-'*50)
print(f'Times em órdem alfabética: {sorted(tabela)}')
print('-'*50)
print(f'O Internacional está na posição {tabela.index('Internacional') + 1}')
