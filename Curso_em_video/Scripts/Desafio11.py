"""
Faça um programa que leia a largura
e a altura de uma parede em metros, 
calcule a sua área e a quantidade
de tinta necessária para pintá-la,
sabendo que cada litro de tinta
pinta uma área de 2m².
area(m²) = alt(m) . larg(m)
"""

alt = float(input('Digite a altura da parede: '));
larg = float(input('Digite a largura da parede: '));

area = alt * larg;

qtdTinta = area / 2;

print('A área da parede é: {}m².\n'
      'Portanto, a quantidade de tinta necessária é de {}L.'.format(area, qtdTinta));