import numpy as np
"""
Ejercicio 1: Lista de equipos

Crea una lista con los 5 primeros equipos de la clasificación (puedes inventar el orden).

Muestra en pantalla el primer y último equipo.

Añade un equipo nuevo al final de la lista.

Inserta a mano un equipo en la primera posición.

Elimina un equipo que ya no quieras que esté en la lista.

---------------------------------------------------------------------------------------------
"""

equipos = ["Betis", "Elche", "Barsa", "Albacete", "Racing de Santander"]

print(equipos[0] + " " + equipos[-1])

equipos.append("Atletico de Bilbao")

equipos[0] = "UD Carrion"

del equipos[2]

print(equipos)


"""
----------
Ejercicio 2: Jornada de partidos

Crea dos listas:
locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]
imprimir los partidos en formato:
Real Madrid vs Athletic
Barcelona vs Betis

Elimina un partido (por ejemplo, el de Sevilla vs Villarreal).
Añade un nuevo partido con un equipo inventado.

--------------------------------------------------------------------------------------------
"""

locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]

for local_index in range(0,len(locales)-1):
  print(locales[local_index]+ " vs "+visitantes[local_index])

del locales[2]
del visitantes[2]

locales.append("Tenerife FC")
visitantes.append("Alcolea FC")

""" 
--------------------------------------------------------------------------------------------
Ejercicio 3: Clasificación de goleadores
Crea una lista con los goles de 6 jugadores:
Muestra cuántos jugadores hay
Ordena la lista de goles de menor a mayor y luego de mayor a menor.
Muestra el máximo y el mínimo de la lista (max() y min()).
Inserta un nuevo jugador con 8 goles en la posición correcta para mantener el orden. 
"""

goles = [20,25,30,34]

numJugadores = len(goles)

print("hay "+ str(numJugadores) + "jugadores")

goles.sort()

print('el minimo de goles es' + str(min(goles)))
print(max(goles))


mi_media = sum(goles)/numJugadores
print('La media es ' + str(mi_media))

media = np.mean(goles)
print(media)



