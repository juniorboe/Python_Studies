"""
Faça um programa que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho
adaptável.

Ex:
escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~~~~~~~~~~
    Olá, Mundo!
~~~~~~~~~~~~~~~~~~~~~~
"""
def escreva(f):
    tamF = len(f) + 4
    
    print('~'*tamF)
    print(f'  {f}')
    print('~'*tamF)

frase = str(input('Digite uma frase: '))
escreva(frase)
