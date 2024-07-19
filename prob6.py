def fibonacci():
    prev = 0
    next = 1
    result = []  # Crea una lista para guardar los numeros
    while prev <= 50:  # Iteramos mientras el numero actual sea menor o igual a 50
        result.append(prev)  # Agregamos el número a la lista
        temp = prev
        prev = next
        next = temp + prev
    print(", ".join(map(str, result)))  # Salida separada por comas

fibonacci()