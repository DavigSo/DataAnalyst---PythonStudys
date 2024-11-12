# FUNÇÕES AVANÇADAS EM PYTHON

# PARAMETROS OPCIONAIS:

# Às vezes, uma função precisa de parâmetros que nem sempre
# são obrigatórios. Podemos definir valores padrão para
# esses parâmetros.

def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")


saudacao("Camille")
saudacao("Camille", "Bom dia")

# FUNÇÕES COM RETORNO DE VALORES

# Funções podem retornar valores paa serem usados em outras
#  partes do código. Isso permite que elas executem cálculos
#  e devolvam o resultado.


def soma(a, b):
    return a + b


resultado = soma(3, 5)
print(resultado)

# FUNÇÕES RECURSIVAS

# Uma função recursiva é aquela que chama a si mesma para
# resolver probemas que podem ser quebrados em subproblemas
# menores.

# EXEMPLO 1


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(5))

# EXEMPLO 2 : Sequencia de fibonacci
# F(0) = 0
# F(1) = 1
# F(n) = F(n -1) + F(n - 2) para n > 1


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Exercicio 1


def cumprimento(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}")


cumprimento("davi")

# Exercicio 2


def multiplicacao(x, y):
    return x * y


resultado = multiplicacao(5, 6)
print(resultado)

# Exercicio 3


def soma_numeros(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + soma_numeros(n - 1)


print(soma_numeros(5))
