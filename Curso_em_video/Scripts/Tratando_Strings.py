"""
frase = 'Curso em Vídeo Python';

frase[9:13] => 'Víde'
frase[9::2] => 'VdoPto'
frase[:9:3] => 'Cse'
len(frase) => é o mesmo que o .lenght do JS
frase.count('o') => mostra quantas vezes existe 'o' na string, então retornará 3
frase.count('o', 0, 13) => mostra quantas vezes existe o 'o' na srting, no intervalo de 0 e 13
frase.find('deo') => mostra o índice onde começa o 'deo'
frase.find('Android') => mostrará -1, que significa que não encontrou 'Android' em frase
'Curso' in frase => responderá com booleano se existe 'Curso' em frase
frase.replace('Python', 'Android') => Substitui 'Python' por 'Android'
frase.upper() => Transforma em maiúscula
frase.lower() =>Transforma em minúscula
frase.captalize() => Transforma a primeira letra da string em maiúscula, e o resto em minúscula
frase.title() => Transforma todas as iniciais de frase em maiúscula, e o resto em minúscula
frase.strip() => Retira os espaços inúteis no início e no final da string
frase.rstrip() => Retira os espaços inúteis do lado direito da string 
frase.lstrip() => Remove os espaços inúteis do lado esquerdo da string 
frase.split() => Cria uma lista a partir do conteúdo da string, considerando cada espaço dela, ['Curso', 'em', 'Vídeo', 'Python']
'-'.join(frase) => 'Curso-em-vídro-Python'
"""