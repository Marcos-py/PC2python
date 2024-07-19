def factorial(n):
  """Calcula el factorial de un número entero positivo"""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")