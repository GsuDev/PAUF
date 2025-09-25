class Persona:

  # Variable estática de clase 
  current = 0

  # Constructor
  def __init__(self, name, last_name, birth_date):
      self.__name = name
      self.__last_name = last_name
      self.__birth_date = birth_date
      
      # Inicializamos los puntos a 0
      self.__points = 0
      
      # Aumenta en uno la id actual de la clase
      Persona.current += 1
      
      # Asigna la id que corresponda al nuevo objeto
      self.__id = Persona.current


  # GETTER Y SETTER
  
  @property
  def name(self):
      return self.__name

  @name.setter
  def _name(self, value):
      self.__name = value

  @property
  def last_name(self):
      return self.__last_name

  @last_name.setter
  def last_name(self, value):
      self.__last_name = value

  @property
  def birth_date(self):
      return self.__birth_date

  @birth_date.setter
  def birth_date(self, value):
      self.__birth_date = value

  @property
  def points(self):
      return self.__points

  @points.setter
  def points(self, value):
      self.__points = value

  @property
  def id(self):
      return self.__id

  @id.setter
  def id(self, value):
      self.__id = value



