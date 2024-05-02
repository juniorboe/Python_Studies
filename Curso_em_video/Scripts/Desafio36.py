"""
Escreva um programa para aprovar o
empréstimo bancário para a compra
de uma casa. O programa vai perguntar
o valor da casa, o salário do
comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30%
do salário ou então o empréstimo
será negado.
"""

print('Bem vindo ao bando x! Siga os passos a seguir para '
      'fazer a solicitação do seu empréstimo!')

valCasa = float(input('Digite o valor da casa: ').strip())
salario = float(input('Digite o valor mensal do salário: ').strip())
anosPag = int(input('Digite qual o prazo anual para o pagamento: ').strip())

prestacao = valCasa / (anosPag * 12)
prestacaoArred = round(prestacao, 2)

if prestacaoArred > salario * 0.30:
    print('\033[1;31mEmpréstimo negado!\033[m\n'
          'Valor da prestação excede 30% do seu salário.')
else:
    print('\033[1;032mEmpréstimo aprovado!\033[m\n'
            'Valor da prestação: R${}'.format(prestacaoArred))