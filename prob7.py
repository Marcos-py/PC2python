def es_perfecto(numero):
    """Verifica si un número es perfecto."""
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

# Encontrar y mostrar los números perfectos menores que 1000
print("Números perfectos menores que 1000:")
for numero in range(1, 1000):
    if es_perfecto(numero):
        print(numero)