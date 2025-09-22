# Manejo de errores

# Bloque try except

try:
  # Aquí lo que pudiera dar error
  print("hola")
  
  resultado1 = 8-10
  
  if resultado1 < 0:
    raise Exception
except Exception as e:
  # Aquí lo que sucede cuando da error
  print("Ha ocurrido un error")
finally:
  # Aquí pasa siempre haya error o no
  print("Esto lo estás viendo si o si al final")