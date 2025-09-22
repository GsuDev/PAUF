'''Empieza a hacerlo aquí'''


ruta = "ddd.log"
contado = 0
f = open(ruta, "r")
print(f.read())

estatitica = "Insert into Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) values ("

with open("Libro.txt", "r") as libro:
    linea = f.readline()
    lineass = ["fran", "alia"]
    formateado = f"{estatitica}{lineass[0]},{lineass[1]}"
    while linea:
        libro.write()
        print(linea, end="")
        f.w
        linea = f.readline()

















#f.close()