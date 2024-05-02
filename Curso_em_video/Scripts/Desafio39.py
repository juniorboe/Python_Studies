"""
Faã um programa que leia o ano de nascimento
de um jovem e informe, de acordo com a sua 
idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do alistamento.

Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo.
"""
import datetime

anoAtual = datetime.date.today().year
anoDeAlistamento = anoAtual - 18
anoNascimento = int(input('Digite o ano do seu nascimento: '))
idade = anoAtual - anoNascimento

if idade < 18:
    print('\033[7;33mAinda não chegou o momento de se alistar.\033[m\n'
          'Idade: {} anos.\nFaltam {} ano(s) para se alistar.'.format(idade, 18 - idade))
elif idade == 18:
    print('\033[7;32mVocê precisa se alistar este ano!\033[m\n'
          'Idade: {} anos.'.format(idade))
elif idade > 18:
    print('\033[7;36mO seu ano de alistamento já passou.\033[m\n'
          'Caso náo tenha se alistado, verifique com a junta mais próxima, e fique em dia com o serviço militar.\n'
          'Idade: {} anos.\nPASSARAM {} ANOS DO SEU ALISTAMENTO!'.format(idade, idade - 18))
