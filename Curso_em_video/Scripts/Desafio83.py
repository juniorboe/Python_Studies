"""
Crie um programa onde o usuário digite uma expressão qualquer que
use parênteses. Seu aplicativo deverá analisar se a expressão
passada está com os parênteses abertos e fechados na ordem correta
"""
expressao = str(input('Digite uma expressão utilizando parênteses: ')) #input da expressão
expSeparada = [] #inicialização da lista que conterá os elementos da expressão separadamente

for i in expressao: #laço que incluirá os elementos do input, na lista da expressão
    expSeparada.append(i)

# A seguir, o código conterá um laço que contará quantos parenteses foram abertos, e quantos foram fechados
contParentesesInicial = 0 
contParentesesFinal = 0

for i in expSeparada:
    if i == "(":
        contParentesesInicial += 1

    if i == ")":
        contParentesesFinal += 1

ordemDoParentese = 0 #Revisão da posição correta dos parênteses no meio da expressão
expCerta = 1
for i in expSeparada:
    if i == '(':
        ordemDoParentese += 1
    if i == ')':
        ordemDoParentese -= 1
        if ordemDoParentese < 0:
            expCerta = 0
            break
        
# Segue a seguir o print de aviso da resolução do desafio
if contParentesesInicial == contParentesesFinal and expCerta == 1:
    print('A expressão foi digitada corretamente!')
else:
    print('A expressão está digitada incorretamente. Por favor, revise-a.')

