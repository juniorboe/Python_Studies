"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
"""
dados = dict()
listaJogadores = []

while True:
    #Lendo o nome do jogador, quantas partidas jogadas
    print('-'*60)
    nome = str(input('Nome do jogador: ')).strip()
    partidas = int(input('Quantidade de partidas: '))

    #Lendo quantos gols foram feitos em cada partida
    gols = []
    totalGols = 0
    for c in range(1, partidas + 1):
        golsPPtd = int(input(f'Gols feitos na partida {c}: '))
        gols.append(golsPPtd)
        totalGols += golsPPtd

    #Calculando aproveitamento do jogador
    aproveitamento = (totalGols / partidas) * 100
    
    #Guardando os dados em um dicionário, incluindo o total de gols feitos durante o campeonato.
    dados['Nome'] = nome
    dados['Partidas'] = partidas
    dados['Gols no campeonato'] = gols
    dados['Total de gols'] = totalGols
    dados['Aproveitamento'] = round(aproveitamento, 1)

    listaJogadores.append(dados.copy())

    dados.clear()

    #Input para confirmar a continuação da lista de jogadores
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while continuar != "S" and continuar != "N":
        continuar = str(input('Erro na digitação. Deseja continuar [S/N]? ')).strip().upper()
    if continuar == "N":
        print('-='*50)
        break

#printando o resultado
#print(' '*4 , 'Id', ' '*2, 'Nome do Jogador', ' '*2, '  Gols no campeonato  ', ' '*3, 'Total de gols', '')
print('    ID   ',end='')
for c in listaJogadores[0]:
    print(f'{c:<20}', end='')
print()
print('-'*100)
for i, c in enumerate(listaJogadores):
    print(' '*2, f'{i:^5}', end='   ')
    for d in c.values():
        print(f'{str(d):<20}', end='')
    print()
print('-'*100)

#Input de qual jogador o usuário quer ver os detalhes

while True:
    idDetalhes = int(input('Qual Jogador você deseja visualizar os detalhes [999 para sair]? '))
    if idDetalhes == 999:
        print('Fechando o programa...')
        break
    while idDetalhes < 0 or idDetalhes > len(listaJogadores) - 1:
        idDetalhes = int(input('Erro na digitação! Qual jogador você deseja visualizar os detalhes [999 para sair]? '))
        if idDetalhes == 999:
            print('Fechando o programa...')
            break
    
    print('-'*100)
    print(f'Informações sobre {listaJogadores[idDetalhes]['Nome']}:\nNúmero de partidas = {listaJogadores[idDetalhes]['Partidas']}.\nAproveitamento: {listaJogadores[idDetalhes]['Aproveitamento']}%.')
    for i, c in enumerate(listaJogadores[idDetalhes]['Gols no campeonato']):
        print(f'No jogo {i + 1} ele fez {c} gols.')
    print('-'*100)
