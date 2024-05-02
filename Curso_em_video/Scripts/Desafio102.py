"""
Crie um programa que tenha uma função fatorial() que
receba dois parâmetros: o primeiro que indique o 
número a calcular e o outro chamado show, que será
um valor lógico(opcional) indicando se será mostrado
ou não na tela o processo de cálculo do fatorial.
"""

"""def fatorial(num, show):
    fat = num
    if show == True:
        print(f'{num}', end=' ')
        for i in range(num-1, 0, -1):
            fat *= i
            print(f'x {i}', end=' ')
        return f'= {fat}'
    else:
        for i in range(num-1, 0, -1):
            fat *= i
        return f'{fat}'"""
def fatorial(num, show=True):
    '''
    ->Faz o cálculo do fatorial de um número
    :param num: número a ser calculado
    :param show: variável booleana opcional para mostrar ou não o cálculo
    :return: se a variável show for True, retorna ou o cálculo do fatorial com o resultado; senão, retorna apenas o resultado do cálculo.
    '''
    if show == True:
        print(f'O cálculo do fatorial de {num} é: \n{num}', end='')
        for i in range(num - 1, 0, -1):
            num *= i
            print(f' x {i}', end='')
        return f' = {num}'
    else:
        for i in range(num-1, 0, -1):
            num *= i
        return f'O resultado do fatorial é: {num}'


#Programa principal
print(fatorial(5, show=True))
help(fatorial)


