"""
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário
com as seguintes informações:

- Quantidade de notas;
- A maior nota;
- A menor nota;

"""

def notas(*n, sit=False):
    '''
    -> Função para analisar as notas, e a situação de um aluno.
    :param n: uma ou mais notas dos alunos (aceita multiplas notas).
    :param sit: quando True, mostra a situação do aluno (False por padrão).
    :return: dicionário com informações das notas e a situação(opcional) do aluno.
    '''

    #Analisando total de notas
    nts['Total de notas'] = len(n)
    
    #analisando maior nota
    maior = 0
    for i in n:
        if i == n[0]:
            maior = i
        else:
            if i > maior:
                maior = i
    nts['Maior nota'] = maior

    #Analisando a menor nota
    menor = maior
    for i in n:
        if i < menor:
            menor = i
    nts['Menor nota'] = menor

    #Analisando a média das notas
    soma = 0
    for i in n:
        soma += i
    media = round(soma/len(n), 1)
    
    nts['Média das notas'] = media

    #Condição para sit=True
    if sit == True:
        if media >= 7:
            nts['Situação'] = 'Boa.'
        elif media < 7 and media > 4.5:
            nts['Situação'] = 'Razoável'
        else:
            nts['Situação'] = 'Ruim.'
                
    return nts


#Programa principal
nts = dict()
print(notas(8, 9, 9.5, sit=True))
help(notas)