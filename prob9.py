#Definimos la función eliminar vocales
def eliminar_vocales(texto):
  vocales = ['a', 'e', 'i', 'o', 'u']
# Usamos una lista para almacenar las consonantes
  consonantes = []
  for letra in texto:
    if letra.lower() not in vocales:
      consonantes.append(letra)  # Agregamos la consonante a la lista
  return ''.join(consonantes)  # Unimos los elementos de la lista en una cadena

texto = input("Ingrese una cadena de texto: ")
texto_sin_vocales = eliminar_vocales(texto)
print("Texto sin vocales:", texto_sin_vocales)