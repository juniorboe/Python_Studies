"""
Faça um programa que leia #nome e #média de um aluno, guardando também
a #situação em um dicionário. No final, mostre o conteúdo da estrutura
na tela.

Para situação:
    Aprovado => Se estiver acima de 7
    Reprovado => Se estiver abaixo de 7
"""

cadastro = {}
cadastro['nome'] = str(input('Nome do aluno: ')).strip()
cadastro['media'] = float(input(f'Média de {cadastro['nome']}: '))

if cadastro['media'] > 0 and cadastro['media'] < 10:
    if cadastro['media'] > 7:
        cadastro['situação'] = 'Aprovado'
    elif cadastro['media'] < 7:
        cadastro['situação'] = 'Reprovado'
else:
    print('Erro na análise da média. Verificar nota.')

#cadastro = {'nome': 'Pedro', 'media': 9}

print(f'\nO nome é igual a {cadastro['nome']}.')
print(f'A média é igual a {cadastro['media']}.')
print(f'A situação é: {cadastro['situação']}.')
