"""
Faça um programa que leia um número
de 0 a 9999 e mostre na tela cada um
dos dígitos separados.
Ex.: Digite um número: 1834

unidade: 4
dezena: 3
centena 8
milhar: 1
"""

"""dig = int(input('Digite um número de 0 a 9999: '));

print('Número digitado: {}'.format(dig));
print('Unidade: {}'.format(dig % 10));
print('Dezena: {}'.format(dig // 10 % 10));
print('Centena: {}'.format(dig // 100 % 10));
print('Milhar: {}'.format(dig // 1000 % 10));

ou
"""
dig = int(input('Digite um número de 0 a 9999: '))
dig = str(dig)

while(len(dig) > 4):
    dig = int(input('O número digitado é maior que 9999! Digite um número de 0 a 9999: '))
    dig = str(dig);

print('Número digitado: {}'.format(dig))

dig.split()
if(len(dig) == 1):
    print('Unidade: {}.\nDezena: -.\nCentena: -.\nMilhar: -.'.format(dig[0]));
elif(len(dig) == 2):
    print('Unidade: {}.\nDezena: {}.\nCentena: -.\nMilhar: -.'.format(dig[1], dig[0]));
elif(len(dig) == 3):
    print('Unidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: -.'.format(dig[2], dig[1], dig[0]));
else:
    print('Unidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: {}.'.format(dig[3], dig[2], dig[1], dig[0]));


"""print('Unidade: {}'.format(dig[0]))
print('Dezena: {}'.format(dig[1]))
print('Centena: {}'.format(dig[2]))
print('Milha: {}'.format(dig[3]))"""
