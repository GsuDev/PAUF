from datetime import datetime
import logging

class Persona:
    """
    Clase base para todos los personajes (héroes y villanos)
    Contiene atributos comunes como nombre, apellidos, fecha de nacimiento, ID y puntuación total
    """
    
    # Variable estática de clase para generar IDs únicos
    current = 0

    def __init__(self, name, last_name, birth_date):
        """
        Constructor de la clase Persona
        
        Args:
            name (str): Nombre de la persona
            last_name (str): Apellidos de la persona
            birth_date (str): Fecha de nacimiento en formato 'YYYY-MM-DD'
        """
        self.__name = name
        self.__last_name = last_name
        self.__birth_date = birth_date
        
        # Inicializar puntos a 0
        self.__points = 0
        
        # Incrementar contador de ID actual
        Persona.current += 1
        
        # Asignar ID único al nuevo objeto
        self.__id = Persona.current
        
        # Registrar creación del personaje en el log
        logging.info(f"Personaje creado: {self.__name} {self.__last_name} con ID {self.__id}")

    # GETTERS Y SETTERS
    
    @property
    def name(self):
        """Obtener el nombre"""
        return self.__name

    @name.setter
    def name(self, value):
        """Establecer el nombre"""
        self.__name = value

    @property
    def last_name(self):
        """Obtener los apellidos"""
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """Establecer los apellidos"""
        self.__last_name = value

    @property
    def birth_date(self):
        """Obtener la fecha de nacimiento"""
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        """Establecer la fecha de nacimiento"""
        self.__birth_date = value

    @property
    def points(self):
        """Obtener la puntuación total"""
        return self.__points

    @points.setter
    def points(self, value):
        """Establecer la puntuación total"""
        self.__points = value

    @property
    def id(self):
        """Obtener el ID único"""
        return self.__id

    @id.setter
    def id(self, value):
        """Establecer el ID único"""
        self.__id = value

    def calculate_age(self):
        """
        Calcular la edad de la persona basada en la fecha de nacimiento
        
        Returns:
            int: Edad en años
        """
        try:
            birth = datetime.strptime(self.__birth_date, '%Y-%m-%d')
            today = datetime.now()
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
            logging.info(f"Edad calculada para {self.__name} {self.__last_name}: {age} años")
            return age
        except ValueError as e:
            logging.error(f"Error calculando edad para {self.__name} {self.__last_name}: {e}")
            return 0

    def __str__(self):
        """Representación en string de la persona"""
        return f"{self.__name} {self.__last_name} (ID: {self.__id}, Edad: {self.calculate_age()}, Puntos: {self.__points})"
