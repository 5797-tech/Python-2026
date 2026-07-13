# Lista de números
numeros = [10, 20, 30, 40]

print("Lista:", numeros)

# Indexação
print("Primeiro:", numeros[0])
print("Último:", numeros[-1])

# Fatiamento
print("Do meio:", numeros[1:3])

# Concatenação
numeros = numeros + [50, 60]
print("Nova lista:", numeros)

# Alterar um valor
numeros[2] = 35
print("Alterada:", numeros)

# Adicionar um valor
numeros.append(70)
print("Com append:", numeros)

# Tamanho da lista
print("Quantidade:", len(numeros))

# Lista aninhada
pares = [2, 4, 6]
listas = [numeros, pares]

print("Lista aninhada:", listas)
print("Primeiro número da segunda lista:", listas[1][0])