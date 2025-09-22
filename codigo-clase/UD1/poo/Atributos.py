class Perro:

    # Atributos de clase
    patas = True

    # Constructor
    def __init__(self, color, especie):
        # Atributos de instancia
        self.color = color
        self.especie = especie

    def ladrar(self):
        print(f'guau guau, mi color es {self.color}')

    def andar(self, metros):
        print(f'El perro ha andado {metros} metros')

    def __str__(self):
       return f"color {self.color} y especie {self.especie}"


zeus = Perro('marron', 'pitbull')
zeus.ladrar()
zeus.andar(10)
zeus.patas = 20

print(zeus.patas)
print(zeus.__str__())