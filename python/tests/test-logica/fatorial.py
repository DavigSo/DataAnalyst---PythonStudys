# crie um programa que receber um numero e imprime o fatorial daquele numero

numero = int(input("Diga um numero: "))
if numero > 0:
    fatorial = 1

    for item in range(1, numero + 1):
        fatorial = fatorial * item
        print(fatorial)
else:
    print(1)
