def es_primo(numero):
    if numero <= 1:
        return False
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Inicializamos con 2 y 3 ya que son primos
suma_primos = 2 + 3
for numero in range(5, 100):
    if es_primo(numero):
        suma_primos += numero

print("La suma de todos los números primos menores que 100 es:", suma_primos)