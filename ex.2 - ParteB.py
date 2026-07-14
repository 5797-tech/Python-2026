# Lista de números
numeros = [25, 12, 8, 40, 17, 30, 5]

print("Lista:", numeros)

# Range
print("\nRange de 10 a 50 de 5 em 5:")
for i in range(10, 51, 5):
    print(i, end=" ")

# Soma
print("\n\nSoma dos números:", sum(numeros))

# Ordenação
print("Ordem crescente:", sorted(numeros))
print("Ordem decrescente:", sorted(numeros, reverse=True))

# Map
quadrado = list(map(lambda x: x**2, numeros))
print("\nQuadrado dos números:")
print(quadrado)

# Filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("\nNúmeros pares:")
print(pares)

# Enumerate
print("\nPosição de cada número:")
for indice, valor in enumerate(numeros):
    print(indice, "->", valor)

# Zip
letras = ["A", "B", "C", "D", "E", "F", "G"]

print("\nAssociação entre letras e números:")
for letra, numero in zip(letras, numeros):
    print(letra, "-", numero)

# Help
print("\nAjuda da função sum:")
help(sum)