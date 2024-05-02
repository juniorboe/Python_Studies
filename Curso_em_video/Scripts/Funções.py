"""
Introdução:

Funções servem para criar rotinas que podem ser usadas a qualquer
momento no código.

Existem funções nativas do Python, como #print(). Porém, é permitido
criar uma função específica para a rotina que queremos através da
lógica criada na rotina.

---------------------------------------------------------------------
Declarção de funções:

- Funções devem ser declaradas sempre no início do código.

- Para declarar uma função:
    def "nomeDaFunção"("possíveisParâmetros"):
        #lógica da função    
        

- As funções podem ter parâmetros, que são dados passados pelo
usuário, e que serão utilizados dentro da mesma.
Ex.:
def soma(n1, n2):
    s = n1 + n2
    print(s)


soma(2, 3) => 5

#Neste caso, os parâmetros foram passados no próprio código, mas 
eles podem ser lidos como inputs.
Ex.:
def soma(n1, n2):
    s = n1 + n2
    print(s)


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma(n1, n2) => 5

#Os parâmetros podem ser explícitos pelo desenvolvedor.
Ex.:
def soma(n1, n2):
    s = n1 + n2
    print(s)


soma(n2 = 3, n1 = 2) => #5
Obs: No momento em que os parâmetros foram explicitados, n2
assume o valor 3, n1 assume o valor 2, e a função segue
funcionando normalmente.
---------------------------------------------------------------------
Empacotamento de parâmetros
Empacotamento serve para fazer a função ler quantos números de 
parâmetros que forem passados pelo usuário, independente da 
quantidade.

O empacotamento retorna uma tupla com o que é pedido na função.
Com isso, podem ser usados todas as funções e métodos utilizados
em tuplas.

Para declarar o empacotamento, basta colocar #* na frente do parâmetro, no
momento da declaração da função.
Ex.:
def contador(*num):
    for v in num:
        print(f'{v}, end='')
    print('Fim')


contador(2, 3, 6, 1) => #2 3 6 1 fim

Ex2.:
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num}, que são ao todo {tam} números.')

    
contador(2, 3, 6, 1) => #Recebi os valores (2, 3, 6, 1), que são ao todo 4 números

---------------------------------------------------------------------
Listas em funções
Funções também podem receber listas como parâmetros. Neste caso,
as listas têm a propriedade de poderem ser alteradas.
Ex.:
def dobra(lst): #lst é chamado de parâmetro formal
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

        
valores = [7, 2, 4, 6] #7, 2, 4, 6 são chamados de parâmetros reais
dobra(valores)
print(valores) => #[14, 4, 8, 12]

---------------------------------------------------------------------
Interative help
Digitando a função #help() e rodando o código, abrirá uma aba no
terminal que permitirá verificar todas as funcionalidades dos
método da linguagem Python.

Pode verificar um método específico colocando ele como parâmetro
da função #help().
Ex.:
help(print)

Obs: Não é necessário utilizar os parênteses dos métodos pesquisados.

---------------------------------------------------------------------
Docstrings
É a documentação em string das funções criadas. Serve para explicar
para outros desenvolvedores, o que as funções criadas podem fazer, os
seus parâmetros, e o seu retorno.
Ex.:
def contador(i, f, p):
    ''' #É necessário usar aspas duplas #" ao invés de simples.
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: paso da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

help(contador)

---------------------------------------------------------------------
Parâmetros opcionais
É quando opcionalmente, é dado valores a parâmetros, para que a função
não retorne um erro por falta de parâmetros reais digitados pelo usuário.
Ex.:
def somar(a, b, c):
    '''
    ->Faz a soma dos valores a, b, c
    :param a: primeiro valor digitado pelo usuário
    :param b: segundo valor digitado pelo usuário
    :param c: terceiro valor digitado pelo usuário
    :return: sem retorno
    '''
    s = a + b + c
    print(f'A soma é {s}')


soma(3, 2) #Retornará erro, pois #c não foi difitado.

para resolver, deve-se utilizar parâmetros opcionais na função.
def somar(a, b, c=0): #para resolver possíveis erros, pode fazer a, b, c = 0.
    '''
    ->Faz a soma dos valores a, b, c
    :param a: primeiro valor digitado pelo usuário
    :param b: segundo valor digitado pelo usuário
    :param c: terceiro valor digitado pelo usuário
    :return: sem retorno
    '''
    s = a + b + c
    print(f'A soma é {s}')


soma(3, 2) #Retornará 5. Pois #c vale 0 por causa do parâmetro opcional.
---------------------------------------------------------------------
Escopo de variável
Basicamente, variáveis que são declaradas dentro da função, tem escopo local,
e variáveis declaradas no bloco de códigos principal, têm escopo global.
Ex.:
def teste(x):
    x+=4 #x assume 5(valor de #a) + 4 
    b = 8
    a = 3 => Este #a tem escopo local.
    print(f'x vale {x}') => #9
    print(f'b vale {b}') => #8
    print(f'a vale {a}') => #3


#Código principal
a = 5 => Este #a tem escopo global.
teste(5)
print(f'a vale {a}') => #5

#Se usar, dentro de uma função, o comando #global (nome_da_variável),
a variável será tratada como global.
Ex.:
def teste(x):
    global a # A variável #a será tratada como variável global.
    x+=4 #x assume 5(valor de #a) + 4 
    b = 8
    a = 3 => Este #a tem escopo local.
    print(f'x vale {x}') => #9
    print(f'b vale {b}') => #8
    print(f'a vale {a}') => #3


#Código principal 
a = 5 => Este #a tem escopo global.
teste(5)
print(f'a vale {a}') => #3
---------------------------------------------------------------------
Retorno de valores
Se não houver retorno, a função apenas retornará dentro dela mesma
Ex.:
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s => #s retorna a resposta para uma variável, ou para um print()

    
#Código principal
r1 = somar(3, 2, 5) => #s retorna para #r1
r2 = somar(2, 2) => #s retorna para #r2
r3 = somar(6) => #s retorna para #r3

print(f'Os resultados foram {r1}, {r2} e {r3}.') #Os resultados foram 10, 4 e 6.

"""