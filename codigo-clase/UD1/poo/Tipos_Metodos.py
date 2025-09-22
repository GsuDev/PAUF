class Robot:

    # Atributo de clase (lo comparten todos los robots)
    bateria = True

    # Constructor
    def __init__(self, modelo, color):
        # Atributos de instancia (cada robot tiene los suyos)
        self.modelo = modelo
        self.color = color

    # Método de instancia
    def hablar(self):
        print(f"Soy el robot {self.modelo}, de color {self.color}")

    def mover(self, pasos):
        print(f"El robot avanza {pasos} pasos")
        self.hablar()

    def pintar_gris(self):
        self.color = "gris"

    # Método de clase
    @classmethod
    def apagar_bateria(cls):
        print("Todas las baterías se han apagado")
        cls.bateria = False

    # Método estático
    @staticmethod
    def version():
        """Método que no accede a atributos de clase ni de instancia"""
        print("Versión de software: 1.0")



r2d2 = Robot("R2-D2", "blanco")
print(r2d2.color)

r2d2.pintar_gris()
print(r2d2.color)

r2d2.mover(10)

# Llamada al método de clase desde la propia clase
Robot.apagar_bateria()
print(Robot.bateria)

# Método estático
Robot.version()