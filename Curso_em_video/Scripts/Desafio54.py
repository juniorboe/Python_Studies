"""
Crie um programa que leia o ano de
nascimento de sete pessoas.
No final, mostre quantas pessoas
ainda não atingiram a maioridade
e quantas já são maiores.
"""
import datetime
#variáveis
anoAtual = datetime.date.today().year
#contadores
contadorMaioridade = 0
contadorMenoridade = 0
#cores
cores = {'limpa': '\033[m', 'cyan': '\033[36m'}
#loop de análise
for i in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)).strip())
    #condicionais de análise
    if (anoAtual - nascimento) >= 21:
        contadorMaioridade += 1
    else:
        contadorMenoridade += 1
#resolução
print('{}Maiores de idade: {} pessoas.\n'
      'Menores de idade: {} pessoas.{}'.format(cores['cyan'], contadorMaioridade, contadorMenoridade, cores['limpa']))