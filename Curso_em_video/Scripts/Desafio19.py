"""
Um professor quer sortear um dos seus
quatro alunos para apagar o quadro.
Faça um programa que ajude ele,
lendo o nome deles e escrevendo o
nome do escolhido.
"""
from random import choice;

nome1 = input('Qual é o nome do primeiro aluno? ');
nome2 = input('Qual é o nome do segundo aluno? ');
nome3 = input('Qual é o nome do terceiro aluno? ');
nome4 = input('Qual é o nome do quarto aluno? ');

alunos = [nome1, nome2, nome3, nome4];

sorteio = choice(alunos);

print('O aluno escolhido é: {}'.format(sorteio));