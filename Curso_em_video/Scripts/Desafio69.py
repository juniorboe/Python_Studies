"""
Crie um programa que leia a idade e o sexo de várias
pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""
#inicializando contadores
count18 = 0
countHomens = 0
countM20 = 0

#loop de cadastro
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()
    while sexo != "M" and sexo != "F":
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()
    if idade > 18:
        count18 += 1
    if sexo == "M":
        countHomens += 1
    if sexo == "F" and idade < 20:
        countM20 += 1
    print('-'*30)
    confirma = str(input('Quer continuar? [S/N] ')).strip().upper()
    while confirma != "S" and confirma != "N":
        confirma = str(input('Quer continuar? [S/N] ')).strip().upper()
    if confirma == "N":
        break
print('='*6, 'FIM DO PROGRAMA', '='*6)
print(f'Total de pessoas com mais de 18 anos: {count18}.')
if countHomens == 1:
    print(f'Ao todo temos {countHomens} homem cadastrado.')
else:
    print(f'Ao todo temos {countHomens} homens cadastrados.')
if countM20 == 1:
    print(f'E temos {countM20} mulher com menos de 20 anos.')
else:
    print(f'E temos {countM20} mulheres com menos de 20 anos.')