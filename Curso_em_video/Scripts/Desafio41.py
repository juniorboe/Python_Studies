"""
A Confederaçã Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre
a sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Digite o ano de nascimento do atleta: ').strip())
idade = anoAtual - anoNascimento
categoria = str('')

if idade > 0 and idade <= 9:
    categoria += 'MIRIM'
    print('Idade: {} anos.\n\033[7mCategoria: {}.\033[m'.format(idade, categoria))
elif idade > 9 and idade <= 14:
    categoria += 'INFANTIL'
    print('Idade: {} anos.\n\033[7mCategoria: {}.\033[m'.format(idade, categoria))
elif idade > 14 and idade <= 19:
    categoria += 'JUNIOR'
    print('Idade: {} anos.\n\033[7mCategoria: {}.\033[m'.format(idade, categoria))
elif idade == 20:
    categoria += 'SÊNIOR'
    print('Idade: {} anos.\n\033[7mCategoria: {}.\033[m'.format(idade, categoria))
elif idade > 20:
    categoria += 'MASTER'
    print('Idade: {} anos.\n\033[7mCategoria: {}.\033[m'.format(idade, categoria))
else:
    print('\033[7;31mIdade incorreta! Fechando o programa...\033[m')
