"""
Faça um programa que leia uma frase
pelo teclado e mostre:

- Quantas vezes aparece a letra 'a';
- Em que posição ela aparece a primeira
vez
- Em que posição ela aparece a última
"""

frase = str(input('Digite uma frase: ')).strip().lower();

print(frase.count("a"));
print(frase.find("a") + 1);
print(frase.rfind("a") + 1);