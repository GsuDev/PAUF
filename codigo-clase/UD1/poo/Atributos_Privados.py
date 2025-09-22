class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):       # Getter
        return self.__nombre

    def set_edad(self, edad):   # Setter con control
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa")



persona = Persona("Francisco", 33)
persona.nombre = "FF"
print(persona.get_nombre())

