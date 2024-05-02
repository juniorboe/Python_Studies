"""
Crie um programa que leia nome, ano de nascimento e carteira de 
trabalho e cadastre-os (com idade) em um dicionário. Se por acaso
a CTPS for diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.
"""
from datetime import date
#Lendo o nome, ano de nascimento e carteira de trabalho
nome = str(input('Nome: ')).strip()
anoNascimento = int(input('Ano de Nascimento: '))
ctps = int(input('Carteira de trabalho (0 = Não tem carteira de trabalho): '))

#Cadastrando os dados (com idade) em um dicionário
anoAtual = date.today().year
idade = anoAtual - anoNascimento

dados = dict()
dados['Nome'] = nome
dados['Idade'] = idade
dados['CTPS'] = ctps

#Adicionando o ano de contratação e o salário, em caso de CTPS != 0
#Calculando com quantos anos a pessoa vai se aposentar. E, acrescentando a #dados

if ctps != 0:
    anoContratacao = int(input('Ano de contratação: '))
    salario = float(input('Salário: '))
    dados['Ano de contratação'] = anoContratacao
    dados['Salário'] = salario
    anoAposentadoria = 35 + dados['Ano de contratação']
    dados['Ano de aposentadoria'] = anoAposentadoria
    #printando dados se CTPS != 0
    print('-='*30)
    for k, v in dados.items():
        print(f'{k}= {v}.')
else: #Se CTPS == 0
    print('-='*30)
    for k, v in dados.items():
        print(f'{k} = {v}')
    print(f'{dados['Nome']} não possui carteira de trabalho.')