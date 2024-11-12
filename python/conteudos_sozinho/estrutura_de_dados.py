# LISTAS

# As listas são usadas para armazenar vários itens em uma
# única variável elas são mutáveis, ou seja, podem ser
# alteradas após a criação.

# Criando uma lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

# Acessando elementos da lista
print(frutas[0])

# Adicionando e removendo itens
frutas.append("uva")
frutas.remove("banana")
print(frutas)

# Iterando sore uma lista
for fruta in frutas:
    print(fruta)

numbers = [1, 2, 3, 4]
numbers.append(8)
numbers.remove(1)
print(numbers)
print(len(numbers))

# TUPLAS

# As tuplas são semelhantes ás listas, mas são imutáveis,
# ou seja, uma vez criads, seus elementos não podem ser
# alterados

# Criando uma tupla
cores = ("vermelho", "azul", "verde")
print(cores)

print(cores[1])

cidade_1 = ("nome1", "habitantes1", "pib1")
cidade_2 = ("nome2", "habitantes2", "pib2")
cidade_3 = ("nome3", "habitantes3", "pib3")
cidades = [cidade_1, cidade_2, cidade_3]

# Iterando pelas cidades e imprimindo as informações com mais clareza
for cidade in cidades:
    nome, habitantes, pib = cidade  # Desempacotando a tupla
    print(f"Nome: {nome}, Habitantes: {habitantes}, PIB: {pib}")


# CONJUNTOS

# Os conjuntos são coleções não ordenadas de itens
# únicos(sem duplicatas). São útris quando vocêquer
# eliminar duplicatas de uma lista ou verificar a presença
# de um item.

# Criando um conjunto
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.remove(2)
print(numbers)


numbers = {1, 2, 33, 4, 4, 5, 5}
print(numbers)

# DICIONARIOS

# Os dicionarios armzenam dados em pares de chave-valor,
# e são úteis quando você quer associar valores a uma
# chave específica.

pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "são paulo"
}

print(pessoa["nome"])
pessoa["idade"] = 31
print(pessoa)

pessoa_2 = {
    "nome": "Davi",
    "idade": 21,
    "cidade": "Campinas"
}
pessoa_2.setdefault("profissão")
pessoa_2["profissão"] = "t.i"
print(pessoa_2)
