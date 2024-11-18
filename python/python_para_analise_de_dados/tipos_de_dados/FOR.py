# O loop FOR do python é usado para travessia sequencial, ou seja, é usado para iterar sobre um iteravel como string, tupla, lista, etc. Ele se enquadra na categoria de iteração definida. Iterações definidas significam que op número de repetições é especificado explecitamente com antecedencia.

for QualquerCoisaQueQuiser in range(1, 11):
    print(QualquerCoisaQueQuiser * 3)

Lista = ["Brasil", "Argentina", 'Uruguai',
         'Paraguai', 'Bolivia', 'Colombia', 'Equador']

for QualquerCoisaQueQuiser in Lista:
    print(QualquerCoisaQueQuiser.upper())
for QualquerCoisaQueQuiser in Lista:
    print(QualquerCoisaQueQuiser.upper()[0:3])

print()
for Pais in Lista:
    if Pais == '  Uruguai':
        print(Pais, 'é Bi campeão da Copa do Mundo!!')
        for NumTitulos in range(2):
            print(NumTitulos)

for Loop in range(0, len(Lista), 2):
    print(Lista[Loop])

for Index, Pais in enumerate(Lista):
    print(Index, Pais)

print()
x = 0
for Paios in Lista:
    print(x, Pais)
    x += 1


Lista = [Numero for Numero in range(0, 10, 2)]
print(Lista)

Lista = []
for Loop in range(0, 10):
    Lista.append(Loop)
    print(Lista)
