# Escreva um programa que, ao iniciar gera um valor aleatrorio de 1 a 10 e permite que o usuario chute um numero até que o valor aleatorio gerado no inicio do programa seja chtuado corretamente

# O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no inicio do programa


from random import randint

valor = randint(1, 10)
chute = 0
while (valor != chute):
    chute = int(input("Chute um numero de 1 a 10: "))

    print("Seu chute foi: ", chute)
    if chute == valor:
        print("Voce acertou")
        print("O valor era: ", valor)
        break
    elif chute < valor:
        print("Chute menor que o valor")
    elif chute > valor:
        print("Chute maior que o valor")
    else:
        print("continue tentando...")
