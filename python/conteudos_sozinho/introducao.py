# CONCEITO 01: VARIAVEIS E TIPOS DE DADOS

# Para se criar variaveis em python, basta dar um nome para
# a variavel e usar o operador = para atribuir um valor a
# ela. Em python, não é preciso declarar o tipo da variavel
# , pois a linguagem entende o tipo automaticamente.

nome = "Camille"  # String
idade = 20  # Int
altura = 1.69  # Float
estudante = True  # boolean

nome = "Nosangela"
idade = 46
altura = 1.65
estudante = False

# CONCEITO 2: OPERADORES ARITMÉTICOS E LÓGICOS

# Os operadores aritméticos servem para fazer calculos
# matematicos. Ja os operadores lógicos são usados para
# criar condições.

a = 10
b = 3
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto_da_divisao = a % b
potencia = a ** b

x = 5
y = 10
print(x == y)
print(x != y)
print(x > 3 and y < 15)
print(not (x > y))

x = 21
y = 20
print(x + y)
print(x - y)
print(x / y)
print(x % y)

# CONCEITO 3: ESTRUTURAS DE CONTROLE(CONDICIONAIS)

# Esses comandos ajudam a criar decisões no seu programa.
# Eles verificam se uma condição é verdadeira ou falsa e
# executam o código de acordo.

idade = 15
if idade >= 18:
    print("Você é maior de idade")

else:
    print("Você é menor de idade.")

# Para mais de uma condição, usamos o elif:

nota = 85

if nota >= 90:
    print("Ótimo")
elif nota >= 70:
    print("Na média")
else:
    print("Precisa melhorar")

temperatura = 31

if temperatura > 30:
    print("Esta quente")
elif temperatura >= 15 and temperatura < 30:
    print("Está agradável")
else:
    print("Está frio!!!")


# CONCEITO 4: ESTRUTURAS DE REPETIÇÃO(LOOPS)

# Os loops permitem repetir uma parte do código várias vezes.
#  Em python, usamos principalmente o while e o for

# While: repete uma ação enquanto uma condição for verdadeira.

contador = 0
while contador < 5:
    print("Contagem: ", contador)
    contador += 1

# For: muito usado para repetir ações um número específico
# de vezes ou para iterar sobre uma coleção
#  de itens(como uma lista).

for i in range(5):
    print("Número: ", i)

# Escreva um programa que usa um loop for para imprimir
#  os números de 1 a 10. Em seguida, modifique para
# imprimir apenas os números pares.
for i in range(10):
    print("Número", i)

# No Python, uma condição if i % 2 avalia True quando i % 2
#  não é zero (ou seja, quando o número é ímpar)
# e False quando é zero (para números pares).
for i in range(10):
    if i % 2:
        print("Números ímpares: ", i)

for i in range(10):
    if i % 2 != 1:
        print("Número pares:", i)


# CONCEITO 5: ESTRUTURA SEQUENCIAL E MODULARIZAÇÃO

# A modularização significa dividir seu código em pequenos
# blocos(ou funções) que realizam tarefas específicas.
# Em python, você cria funções usando def.

def saudacao(nome):
    print("Olá,", nome)


saudacao("ana")


def soma(a, b):
    print(a + b)


soma(12, 4)
