# Pedir al usuario la cantidad de alumnos
n = int(input("Ingrese la cantidad de alumnos: "))

# Inicializar la lista para guardar los datos de los alumnos
alumnos = []

# Ingresar los datos de los alumnos
for i in range(n):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        # Se elimina la validación de ValueError
        nota = int(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos.append({"Alumno": nombre, "Notas": notas})

# Mostrar el listado de alumnos
for alumno in alumnos:
    print(alumno)