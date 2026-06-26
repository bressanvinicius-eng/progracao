def calcular_media(numeros):
    # A função sum() soma todos os elementos e len() retorna o tamanho da lista
    soma = sum(numeros)
    return soma / len(numeros)

# No Python, usamos listas em vez de arrays fixos
numeros = [10, 20, 30, 40, 50]

media = calcular_media(numeros)

# O f-string com :.2f formata o resultado para duas casas decimais
print(f"A média é: {media:.2f}")
