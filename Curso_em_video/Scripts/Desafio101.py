"""
Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
nas eleições.
"""

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18 and idade < 65:
        return f'Idade: {idade} anos. Voto Obrigatório.'
    elif (idade >= 16 and idade < 18) or idade >= 65:
        return f'Idade: {idade} anos. Voto Opcional.'
    elif idade > 0 and idade < 16:
        return f'Idade: {idade} anos. Voto negado.'
    else:
        return f'ERRO! Idade digitada é menor que 0.'


#Programa principal
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))