"""
Crie um programa que tenha uma tupla com
várias palavras (não usar acentos).
Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
"""
palavras = ('Boomerang', 'Cachorro', 'Computador')

for palavra in palavras:
    palavraMinuscula = palavra.lower()
    print(f'\nNa palavra {palavra} temos as vogais:', end=' ')
    for letra in palavraMinuscula:
        if letra in 'aeiou':
            print(letra, end=' ')

"""    
    for letra in palavraMaiuscula:
    if letra == 'A':
        print('A', end=' ')
    elif letra == 'E':
        print('E', end=' ')
    elif letra == 'I':
        print('I', end=' ')
    elif letra == 'O':
        print('O', end=' ')
    elif letra == 'U':
        print('U', end=' ')
"""