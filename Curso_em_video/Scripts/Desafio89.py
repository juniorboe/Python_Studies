"""
Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a
média de cada um e permita que o usuário possa mostrar as notas de
cada aluno individualmente.
"""
from time import sleep

cadastro = []
alunos = []
notas = []
id = 0
while True:
    aluno = str(input('Digite o nome do aluno: ')).strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    
    alunos.append(id)
    if aluno not in alunos:
        alunos.append(aluno)
    notas.append(nota1)
    notas.append(nota2)
    alunos.append(media)
    alunos.append(notas[:])
    cadastro.append(alunos[:])
    alunos.clear()
    notas.clear()

    id += 1
    print('Cadastrando aluno...')
    sleep(0.7)
    print('Aluno cadastrado com sucesso!\n')

    continuar = str(input('Deseja cadastrar mais algum aluno? [S/N]')).strip().upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input('Erro na digitação. Deseja cadastrar mais algum aluno? [S/N]')).strip().upper()
    if continuar == "N":
        break
print('\n')
print('-='*14)
print('ID', ' '*2, 'Nome do aluno', ' '*2, 'Média')
print('-'*28)
for pos, c in enumerate(cadastro):
    print(f'{cadastro[pos][0]:^2}',' '*2, f'{cadastro[pos][1]:^13}', ' '*2, f'{cadastro[pos][2]:^5}', end='\n')
print('-'*28)

while True:
    mostrar = int(input('\nDigite o ID do aluno para acessar as suas notas. (Digite 999 para sair do programa)'))

    while (mostrar > len(cadastro) - 1 or mostrar < 0) and mostrar != 999:
        mostrar = int(input('ID não encontrado! Digite novamente: '))
        if mostrar == 999:
            break
    if mostrar == 999:
        print('\nFechando o banco de cadastro.')
        break
    
    print('\nAcessando notas do aluno...\n')
    sleep(0.7)
    print(f'Aluno: {cadastro[mostrar][1]}.\nNota 1: {cadastro[mostrar][3][0]}.\nNota 2: {cadastro[mostrar][3][1]}.')
