# Definimos la clase
class Edificio:
  
  # Constructor de la clase
  def __init__(self, puertas, plantas, ventanas = None):
    self.__puertas = puertas
    self.__plantas = plantas
    self.__ventanas = ventanas
  
  
  def set_ventanas(self, ventanas):
    self.__ventanas = ventanas
  
  def get_ventanas(self):
    return self.__ventanas
  
  # to string
  def __str__(self):
    return f"Hay {self.__puertas} puertas y {self.__ventanas} ventanas"
  


edificio = Edificio(10, 40, 30)
print(edificio.get_ventanas())
edificio.set_ventanas(60)
print(edificio.get_ventanas())

class Persona:
  def __init__(self, dni, nombre, apellidos):
    self._dni = dni
    self._nombre = nombre
    self._apellidos = apellidos
  
  def identificacion(self):
    return f"Soy {self._nombre} {self._apellidos}"
  
  def identificacion1(self):
    return f"Soy {self._nombre} {self._apellidos}"
  

class Vendimiador(Persona):
  def __init__(self, dni, nombre, apellidos, uvas):
    self._dni = dni
    self._nombre = nombre
    self._apellidos = apellidos
    self._uvas = uvas
    super().__init__(dni, nombre, apellidos)
  
  def identificacion(self):
    iden_padre = super().identificacion()
    return f"{iden_padre} y he pillao {self._uvas} uvas"
  
  def identificacion1(self):
    return "Soy dj totote"
  
  
  
  
  
paquito = Vendimiador("1A", "Paco", "Perez", 70)

print(paquito.identificacion())
print(paquito.identificacion1())
