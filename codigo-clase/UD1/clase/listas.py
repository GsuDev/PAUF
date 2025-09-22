dias = []
#Append Añade un único elemento al final de la lista.
dias.append("Lunes")
dias.append("Martes")
dias.append("Miercoles")
print(dias)
#Remove Remueve la primer coincidencia del elemento especificado.
dias.remove("Martes")
print(dias)
print("CORTO")
elem = dias.pop()
print(elem)
print(dias)

print(dias[-1])
fines_semana =['Sabado', 'Domingo']
#extends Añade otra lista al final de una lista.
dias.extend(fines_semana)
print("Ya esta la lista")
print(dias)

#del Elimina el elemento ubicado en el indice descrito
numeros = [1,2,3,4,5,6]
del numeros[1]
print(numeros)
del numeros[:2]
print(numeros)

#insert Inserta un nuevo elemento en una posición determinada de la lista
numeros.insert(0,10)
print(numeros)

#Sort para ordenar
numeros.sort()
print("Voy a imprimir ordenado")
print(numeros)
numeros.sort(reverse=True)
print(numeros)

