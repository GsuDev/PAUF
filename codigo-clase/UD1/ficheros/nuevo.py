from datetime import datetime
nombre = "Francisco"
fecha = datetime.now().strftime("%d%m%Y").lower()
nombre_fichero = f"log/{fecha}{nombre}_Persona.log"


print(fecha)
with open(nombre_fichero, "w") as f:
    f.writelines("Hola")