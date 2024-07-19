Lista_mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def convertir_fecha(fecha_str):
  mes, dia, año = fecha_str.split('/')
  mes_num = int(mes)
  return f"{año}-{mes_num:02d}-{int(dia):02d}"  # Formato AAAA-MM-DD con ceros a la izquierda

fecha_str = input("Ingrese una fecha en formato mes/día/año: ")
fecha_convertida = convertir_fecha(fecha_str)
print(fecha_convertida)