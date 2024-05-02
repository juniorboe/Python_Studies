"""
Desenvolva uma lógica que leia o peso e a altura de uma
pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:

- Abaixo  de 18.5: Abaixo do peso.
- Entre 18.5 e 25: peso ideal.
- Entre 25 até 30: Sobrepeso.
- Entre 30 até 40: Obesidade grau 1.
- Acima de 40: Obesidade grau 2.
"""

peso = float(input('Digite o peso em kilos: ').strip())
altura = float(input('Digite a altura em centímetros: ').strip())

calculoImc = peso / ((altura / 100) ** 2)
imc = round(calculoImc, 2)
status = str('')
print(imc)

if imc > 0 and imc < 18.5:
    status += 'Abaixo do peso.'
    print('IMC: {}.\nStatus: {}'.format(imc, status))
elif imc >= 19.5 and imc < 25:
    status += 'Peso ideal.'
    print('IMC: {}.\nStatus: {}'.format(imc, status))
elif imc >= 25 and imc < 30:
    status += 'Acima do peso.'
    print('IMC: {}.\nStatus: {}'.format(imc, status))
elif imc >= 30 and imc <= 40:
    status += 'Obesidade grau 1.'
    print('IMC: {}.\nStatus: {}'.format(imc, status))
elif imc > 40:
    status += 'Obesidade grau 2.'
    print('IMC: {}.\nStatus: {}'.format(imc, status))
else:
    print('\033[7;31mErro na leitura de informações. Fechando o programa...\033[m')
