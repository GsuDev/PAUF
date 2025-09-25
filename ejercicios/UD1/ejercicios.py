
class Alumno:
    def __init__(self, nombre, edad, clase):
        self.nombre = nombre
        self.edad = edad
        self.clase = clase

    
    
    def __str__(self):
        return f"Alumno({self.nombre}, {self.edad}, {self.clase})"



alumnos = [
    Alumno("Francisco", 20, "DAW"),
    Alumno("Ana", 21, "DAM"),
    Alumno("Luis", 19, "DAW"),
]

'''
Actividad 1. Realizar un metodo de busqueda para buscar en la lista de alumnos, por el nombre de alguno de los elementos que se encuentra en la lista
Actividad 2. Mediante el uso de getattr realizar un metodo general para buscar sobre cualquier atributo de una lista de objetos pasandole como parametro
el nombre del atributo y el valor a buscar.
Actividad 3. Aula, entregable.
'''

def alumno_por_nombre(alumnos, nombre):
  for alumno in alumnos:
    if alumno.nombre == nombre:
      return alumno

# Funcion que recibe una lista de alumnos, un atributo y un valor y devuelve el alumno que coincide
def alumno_por_atributo(lista_alumnos, atributo: str, valor):
  for alumno in lista_alumnos:
    # Aqui un try except
    
    if getattr(alumno, atributo) == valor:
      return alumno



print(alumno_por_nombre(alumnos, 'ana'))
print(alumno_por_atributo(alumnos,'edad', 21))