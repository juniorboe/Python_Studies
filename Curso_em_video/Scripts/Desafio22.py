"""
Crie um programa que leia o nome completo
de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (Sem considerar
espaços)
- Quantas letras tem o primeiro nome
"""

nome = str(input('Digite o seu nome completo: ')).strip();

print(nome.upper());
print(nome.lower());
dividido = nome.split();
junto = ''.join(dividido);
print(len(junto));
print(len(dividido[0]));