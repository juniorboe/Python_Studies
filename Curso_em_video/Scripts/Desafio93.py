"""
Crie um programa que gerencie o aproveitamento de um jogador de 
futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
"""
dados = dict()
#Lendo o nome do jogador, quantas partidas jogadas
nome = str(input('Nome do jogador: ')).strip()
partidas = int(input('Quantidade de partidas: '))

#Lendo quantos gols foram feitos em cada partida
gols = []
totalGols = 0
for c in range(1, partidas + 1):
    golsPPtd = int(input(f'Gols feitos na partida {c}:'))
    gols.append(golsPPtd)
    totalGols += golsPPtd

#Calculando aproveitamento do jogador
aproveitamento = (golsPPtd / partidas)


#Guardando os dados em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados['Nome do jogador'] = nome
dados['Partidas'] = partidas
dados['Gols no campeonato'] = gols
dados['Aproveitamento'] = aproveitamento

#printando o resultado de #dados
print('-='*30)
for k, v in dados.items():
    if k == 'Aproveitamento':
        print(f'    {k} = {v:.1%}')
    else:
        print(f'    {k} = {v}.')
print('-='*30)

#Printando os gols por partida, e o total de gols
for c in range(1, partidas + 1):
    print(f'Na partida {c}, fez {dados['Gols no campeonato'][c - 1]}')
print(f'Foi um total de {totalGols} gols.')

