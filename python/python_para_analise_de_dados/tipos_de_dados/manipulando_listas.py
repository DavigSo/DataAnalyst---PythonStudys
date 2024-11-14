Lista_Vazia = []
print(Lista_Vazia)

Lista_Vazia.append(1)
Lista_Vazia.append(2)
Lista_Vazia.append(3)
Lista_Vazia.append('Valor')
print(Lista_Vazia)

# Acessar
print()
print(Lista_Vazia)
Lista_Vazia.clear()
print(Lista_Vazia)

print()

# Inserir por posição
Lista_Vazia.insert(0, '1.5')
print(Lista_Vazia)
print()
# Função extends
Lista_01 = [1, 2, 3]
Lista_02 = [4, 5, 6]
Lista_01.extend(Lista_02)
print(Lista_01)
print()
# pop - remover
Lista_01.pop(0)
print(Lista_01)
print()

# Sort - ordenação
Lista_ABC = ['z', 'c', 'f', 'H', 'A']
Lista_ABC.sort
print(Lista_ABC)
print()

# Identificador de valor
print(Lista_ABC.index('H'))
