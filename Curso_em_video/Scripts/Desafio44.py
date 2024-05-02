"""
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e
condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.
"""

valorProd = float(input('Qual é o valor do produto: ').strip())
valorFinal = 0
metPag = int(input('Qual é o método de pagamento: \n'
                   '1- À vista (dinheiro/cheque).\n'
                   '2- À vista no cartão de débito.\n'
                   '3- Cartão de crédito.\n').strip())

while metPag < 1 or metPag > 3:
    print('\033[31mEntrada incorreta!\033[m\n')
    metPag = int(input('Qual é o método de pagamento: \n'
                   '1- À vista (dinheiro/cheque).\n'
                   '2- À vista no cartão de débito.\n'
                   '3- Cartão de crédito.\n').strip())
if metPag == 1:
    valorFinal = valorProd * 0.90
    print('Método: À vista.\nValor a ser pago: R${:.2f}.'.format(valorFinal))
elif metPag == 2:
    valorFinal = valorProd * 0.95
    print('Método: À vista (débito).\nValor a ser pago: R${:.2f}.'.format(valorFinal))
elif metPag == 3:
    parcelas = int(input('Em quantas parcelas será o pagamento (1 a 10):\n').strip())
    
    while parcelas < 1 or parcelas > 10:
        print('\033[31mEntrada incorreta!\033[m')
        parcelas = int(input('Em quantas parcelas será o pagamento (1 a 10):\n').strip())
    
    if parcelas == 1:
        valorFinal = valorProd
        print('Método: Cartão de crédito ({}x).\nValor a ser pago: R${:.2f}.'.format(parcelas, valorFinal))
    elif parcelas == 2:
        valorFinal = valorProd
        print('Método: Cartão de crédito ({}x).\nValor a ser pago: R${:.2f}.\n'
              'Valor da parcela: R${:.2f}'.format(parcelas, valorFinal, valorFinal/parcelas))
    else:
        valorFinal = valorProd * 1.20
        print('Método: Cartão de crédito ({}x).\nValor a ser pago: R${:.2f}.\n'
              'Valor da parcela: R${:.2f}'.format(parcelas, valorFinal, valorFinal/parcelas))

