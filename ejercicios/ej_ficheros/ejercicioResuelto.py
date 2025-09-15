from datetime import datetime

# Creo la matriz users
users = []

# Abro el archivo donde estan los datos
with open("/Users/gsu/Documents/GitHub/PAUF/apuntes/ficheros/Libro2.txt", "r") as f:
  
  # Leo la primera linea 
  linea = f.readline()
  
  # Mientras hayan lineas
  while linea:
    
    # Guardo en userData los datos de la linea en forma de vector separandolos segun los espacios
    userData = linea.split(' ')
    
    # Añado el vector a la matriz de usuarios
    users.append(userData)
    
    # Imprime por consola los datos del usuario para trazabilidad
    print(linea)
    
    # Lee la siguiente linea
    linea = f.readline()


# Guarda la fecha y hora en forma de string
ahora = str(datetime.now())

# Crea un txt con la fecha de ahora con permiso de adicion al final
with open(f'/Users/gsu/Documents/GitHub/PAUF/apuntes/ficheros/{ahora}.txt', "a") as fr:
  
  # Recorre las filas (usuarios) de la matriz
    for user in users:
      
      # El ultimo dato de cada fila es un salto de linea que debemos eliminar
      user.pop()
      
      # Escribe la parte estática de la linea del documento de destino
      fr.write('Insert into Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) values ( ')
      
      # Recorre las columnas (datos) de la fila (usuario)
      for field in user:
        # Escribe el dato en el documento, seguido de una coma
        fr.write(field+', ')
      
      # Escribe el parentesis final y el salto de linea
      fr.write(')\n')


#Buen trabajo, escalable y muy claro. Tenemos que ver lo de las rutas y otra cosa los archivos no puedes nombrarlos con dos puntos por eso he formateado yo solo con dia, mes y año. En mac no se si te deja
#pero en linux por ejemplo que es el so que se usa para desplegar aplicaciones que es donde van a estar los logs, no se come. Quita hora, luego mas adelante os enseño a que cada vez que insertemos una linea de log se pone la hora.
#Pero muy bien
