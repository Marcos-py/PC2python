# Variables para contar números pares e impares
numeros_ingresados = []
numeros_pares = 0
numeros_impares = 0
# Bucle para ingresar números
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
        numeros_ingresados.append(numero)
    elif respuesta == "NO":
        break
# Mostrar resultados
print(f"Números ingresados: {numeros_ingresados}")
print(f"Cantidad de números pares: {numeros_pares}")
print(f"Cantidad de números impares: {numeros_impares}")