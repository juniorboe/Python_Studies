"""
Crie um programa que leia duas notas de um aluno e
calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO.
- Média entre 5.0 e 6.9: RECUPERAÇÃO.
- Média 7.0 ou superior: APROVADO.
"""

nota1 = float(input('Digite a primeira nota: ').strip())
nota2 = float(input('Digite a segunda nota: ').strip())

media = (nota1 + nota2) / 2

if media > 0 and media < 5.0:
    print('\033[31mREPROVADO!\033[m\n'
          'Nota: {}.'.format(media))
elif media >= 5.0 and media < 7.0:
    print('\033[33mRECUPERAÇÃO.\033[m\n'
          'Nota: {}.'.format(media))
elif media >= 7.0 and media <= 10:
    print('\033[32mAPROVADO!\033[m\n'
          'Nota: {}.'.format(media))
else:
    print('\033[7;31mERRO! Fechando o programa...\033[m')
