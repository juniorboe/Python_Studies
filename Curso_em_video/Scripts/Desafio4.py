"""Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações
possíveis sobre ele."""

algo = input('Escreva algo: ');
print(algo);
print('{} é alfanumérico? {}'.format(algo, algo.isalnum()));
print('{} é dígito? {}'.format(algo, algo.isdigit()));
print('{} é numérico? {}'.format(algo, algo.isnumeric()));
print('{} é alfabético? {}'.format(algo, algo.isalpha()));
print('{} está todo em letras maiúsculas? {}'.format(algo, algo.isupper()));
print('{} está todo em letras minúsculas? {}'.format(algo, algo.islower()));
print('{} só tem espaços? {}'.format(algo, algo.isspace()));