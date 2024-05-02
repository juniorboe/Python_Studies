"""
Faça um programa que leia o sexo de uma 
pessoa, mas só aceite os valores 'M' 
ou 'F'. Caso esteja errado, peça a 
digitação novamente até ter um valor
correto.
"""
sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('\033[31mERRO DE DIGITAÇÃO!\033[m')
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
if sexo == 'M':
    print('O sexo da pessoa é masculino.')
else:
    print('O sexo da pessoa é feminino.')