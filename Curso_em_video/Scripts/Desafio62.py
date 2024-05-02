"""
Melhore o DESAFIO 061, perguntando para o usuário
se ele quer mostrar mais alguns termos. O 
programa encerra quando ele disser que quer 
mostrar 0 termos.
"""

#Variáveis
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
count = 1

#loop de cálculo
print(termo, end=' ')
while count < 10:
    termo += razao
    count += 1
    print('{}'.format(termo),end=' ')
print('Pausa')
novoCount = int(input('\nQuantos termos mais você quer mostrar? \n'))
while novoCount > 0:
    print('Você escolheu mostrar {} termos a mais.'.format(novoCount))
    count = novoCount
    while count > 0:
        termo += razao
        count -= 1
        print(termo, end=' ')
    print('Pausa')
    novoCount = int(input('\nQuantos termos mais você quer mostrar? \n'))
print('Acabou!')