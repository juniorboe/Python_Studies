"""
While - do while
Usada quando não se sabe quando terminar o loop.

Usa-se o break para parar um loop infinito.
ex:
    num = soma = 0
    while True:
        num = int(input('Digite um número inteiro: '))
        if num == 999:
            break
        soma += num
    print(f'A soma vale: {soma}.')
     
"""