"""
Desenvolva um programa que leia as
duas notas de um aluno, calcule
e mostre a sua média.
CUIDAR A ORDEM DE PRECEDÊNCIA!
"""

nota1 = float(input('Digite a primeira nota: '));
nota2 = float(input('Digite a segunta nota: '));

med = (nota1 + nota2) / 2;

print('Nota 1 = {:.2f}.\n'
      'Nota 2 = {:.2f}.\n'
      'A média do aluno é: {:.2f}'.format(nota1, nota2, med));