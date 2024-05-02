n1 = int(input('Digite um número: '));
n2 = int(input('Digite outro número: '));

soma = n1 + n2;
subt = n1 - n2;
div = n1 / n2;
mult = n1 * n2;
pot = n1 ** n2;
res = n1 % n2;
divInt = n1 // n2;

print('A soma é {}. \nA subtração é: {}. \nA divisão é: {:.3f}.'
      '\nA multiplicação é: {}. \nA potência é: {}. '
      '\nO resto é: {}. \nA divisão inteira é: {}.'.format(soma, subt, div, mult, pot, res, divInt));