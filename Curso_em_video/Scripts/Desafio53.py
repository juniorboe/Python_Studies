"""
Crie um programa que leia uma frase
qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
"""
frase = str(input('Digite uma frase: ').upper().strip())
fraseIndex = ''
fraseInvertida = frase[::-1]
fraseInvertidaIndex = ''
for i in frase:
    if i != ' ':
        fraseIndex += i
for i in fraseInvertida:
    if i != ' ':
        fraseInvertidaIndex += i

if fraseIndex == fraseInvertidaIndex:
    print('\033[32mA frase é um palígono.\033[m')
else:
    print('\033[31mA frase não é um palígono.\033[m')
"""
ou
palavras = frase.split()
fraseJunta = ''.join(palavras)
fraseInvertida = fraseJunta[::-1]

if fraseJunta == fraseInvertida:
    print('{} é igual a {}. Portanto, é um palíndromo!'.format(fraseJunta, fraseInvertida))
else:
    print('{} não é igual a {}. Portanto, não é um palíndromo.'.format(fraseJunta, fraseInvertida))
"""