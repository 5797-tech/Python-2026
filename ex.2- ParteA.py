# Lista de letras
letras = ["A", "B", "C", "D"]

# Lista de números
numeros = [10, 20, 30, 40]

print("Lista de letras:", letras)
print("Lista de números:", numeros)

# Indexação
print("Primeira letra:", letras[0])
print("Último número:", numeros[-1])

# Fatiamento
print("Letras do meio:", letras[1:3])
print("Primeiros 3 números:", numeros[:3])

# Concatenação
letras = letras + ["E", "F"]
numeros = numeros + [50, 60]

print("Letras atualizadas:", letras)
print("Números atualizados:", numeros)

# Alterar valores
letras[2] = "Z"
numeros[1] = 25

print("Letras alteradas:", letras)
print("Números alterados:", numeros)

# Adicionar novos elementos
letras.append("G")
numeros.append(70)

print("Letras com append:", letras)
print("Números com append:", numeros)

# Tamanho das listas
print("Total de letras:", len(letras))
print("Total de números:", len(numeros))

# Lista aninhada
dados = [letras, numeros]

print("Lista aninhada:", dados)

# Aceder a elementos da lista aninhada
print("Primeira letra:", dados[0][0])
print("Terceiro número:", dados[1][2])
