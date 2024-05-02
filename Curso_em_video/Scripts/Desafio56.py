"""
Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do
programa, mostre: 

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
#cores
cores = {'limpa': '\033[m', 'vermelho': "\033[31m", 'verde': '\033[32m', 'amarelo': '\033[33m'}

#variáveis
somaIdade = 0
maiorIdade = 0
homemMaisVelho = ''
contadorM20 = 0

#loop de captação dos dados
for i in range(1, 5):
    print('------ {}ª pessoa ------'.format(i))
    nome = str(input('\n{}Digite o nome da {}ª pessoa: {}'.format(cores['amarelo'], i, cores['limpa'])).strip())
    idade = int(input('{}Digite a idade da {}ª pessoa: {}'.format(cores['amarelo'], i, cores['limpa'])).strip())
    #loop de correção de erro de digitação (idade menor que 0)
    while idade < 0:
        idade = int(input('{}ERRO DE DIGITAÇÃO! Idade menor que 0.\n{}Digite a idade da {}ª pessoa: {}'.format(cores['vermelho'], cores['amarelo'], i, cores['limpa'])).strip())

    sexo = str(input('{}Digite o sexo da {}ª pessoa\n(M para masculino e F para feminino): {}'.format(cores['amarelo'], i, cores['limpa'])).strip())
    #loop de correção do erro de digitação
    while sexo != "M" and sexo != "F":
        sexo = str(input('{}ERRO DE DIGITAÇÃO!{}\nDigite o sexo da {}ª pessoa\n(M para masculino e F para feminino): {}'.format(cores['vermelho'], cores['amarelo'], i, cores['limpa'])).strip())
    
    somaIdade += idade
    #condicionais (homemMaisVelho)
    if i == 1 and sexo == "M":
        homemMaisVelho = nome
        maiorIdade = idade
    elif sexo == "M" and idade > maiorIdade:
        maiorIdade = idade
        homemMaisVelho = nome

    #condicional (mulheres com menos de 20 anos)
    if sexo == "F" and idade < 20:
        contadorM20 += 1

#resolução
        
mediaIdade = somaIdade / 4
print('\n{}A média de idade do grupo é: {:.1f} anos.\n'
    'O nome do homem mais velho do grupo é: {}.\n'
    'A quantidade de mulheres do grupo com menos de 20 anos é: {}.{}'.format(cores['verde'], mediaIdade, homemMaisVelho, contadorM20, cores['limpa']))
