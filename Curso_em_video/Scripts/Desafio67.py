"""
Faça um programa que mostre a tabuada de vários 
números, um de cada vez, para cada valor digitado 
pelo usuário. O programa será interrompido quando o 
número solicitado for negativo.
"""
#Inicializando variáveis
num = tabuada = 0
#loop de criação de tabuadas
while True:
    num = int(input('Digite um númedo e saiba a sua tabuada: '))
    if num < 0:
        print('Flag encontrada, programa finalizado!')
        break
    print('-'*30)
    count = 1
    while count <= 10:
        tabuada = num * count
        print(f'{count:2} x {num} = {tabuada}')
        count += 1
    print('-'*30)
