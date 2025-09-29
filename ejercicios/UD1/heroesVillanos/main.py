#!/usr/bin/env python3

import logging
from gestor import GestorPersonajes

"""
Sistema de Gestión de Héroes y Villanos
=================================
Hay un menú principal con opciones para crear, listar, buscar y emparejar personajes.
Cada personaje tiene traits aleatorios que afectan su puntuación total.
El sistema registra todas las operaciones en un archivo de log.

Faltan cosas porque he estado malo
"""



def mostrar_menu():
    """
    Muestra el menú principal del sistema
    """
    print("\n" + "=" * 60)
    print("   SISTEMA DE GESTIÓN DE HÉROES Y VILLANOS")
    print("=" * 60)
    print("1. Crear Héroe")
    print("2. Crear Villano")
    print("3. Listar todos los Héroes")
    print("4. Listar todos los Villanos")
    print("5. Buscar Héroe por atributo")
    print("6. Buscar Villano por atributo")
    print("7. Consultar edad de un personaje")
    print("8. Emparejar Héroe y Villano aleatoriamente")
    print("9. Ver estadísticas del sistema")
    print("0. Salir")
    print("=" * 60)


def crear_heroe(manager):
    print("\n--- CREAR NUEVO HÉROE ---")
    try:
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()

        if not nombre or not apellidos or not fecha_nacimiento:
            print("❌ Error: Todos los campos son obligatorios")
            return

        hero = manager.create_hero(nombre, apellidos, fecha_nacimiento)
        if hero:
            print(f"\n✓ Héroe creado exitosamente!")
            print(f"  {hero}")
        else:
            print("❌ Error al crear el héroe")
    except Exception as e:
        print(f"❌ Error: {e}")


def crear_villano(manager):
    print("\n--- CREAR NUEVO VILLANO ---")
    try:
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()

        if not nombre or not apellidos or not fecha_nacimiento:
            print("❌ Error: Todos los campos son obligatorios")
            return

        villain = manager.create_villain(nombre, apellidos, fecha_nacimiento)
        if villain:
            print(f"\n✓ Villano creado exitosamente!")
            print(f"  {villain}")
        else:
            print("❌ Error al crear el villano")
    except Exception as e:
        print(f"❌ Error: {e}")


def listar_heroes(manager):
    print("\n--- LISTA DE HÉROES ---")
    heroes = manager.get_all_heroes()

    if not heroes:
        print("No hay héroes registrados en el sistema")
        return

    print(f"Total de héroes: {len(heroes)}\n")
    for hero in heroes:
        print(f"  {hero}")


def listar_villanos(manager):
    print("\n--- LISTA DE VILLANOS ---")
    villains = manager.get_all_villains()

    if not villains:
        print("No hay villanos registrados en el sistema")
        return

    print(f"Total de villanos: {len(villains)}\n")
    for villain in villains:
        print(f"  {villain}")


def buscar_heroe(manager):
    print("\n--- BUSCAR HÉROE ---")
    print("Atributos básicos: name, last_name, id, points")
    print("Traits: CodigoLimpio, BienDocumentado, GITGod, Arquitecto, Detallista")

    atributo = input("\nAtributo a buscar: ").strip()
    valor = input("Valor a buscar: ").strip()

    print("\nTipo de comparación:")
    print("1. Igual (=)")
    print("2. Mayor que (>)")
    print("3. Menor que (<)")

    opcion_comp = input("Selecciona tipo (1-3): ").strip()

    comparacion = "equal"
    if opcion_comp == "2":
        comparacion = "greater"
        try:
            valor = float(valor)
        except ValueError:
            print("❌ Error: El valor debe ser numérico para comparaciones > o <")
            return
    elif opcion_comp == "3":
        comparacion = "less"
        try:
            valor = float(valor)
        except ValueError:
            print("❌ Error: El valor debe ser numérico para comparaciones > o <")
            return

    resultados = manager.search_heroes_by_attribute(atributo, valor, comparacion)

    print(f"\n--- RESULTADOS DE BÚSQUEDA ---")
    print(f"Se encontraron {len(resultados)} héroe(s):\n")

    if resultados:
        for hero in resultados:
            print(f"  {hero}")
    else:
        print("  No se encontraron héroes con esos criterios")


def buscar_villano(manager):
    print("\n--- BUSCAR VILLANO ---")
    print("Atributos básicos: name, last_name, id, points")
    print("Traits: Chagepeteador, EntregadorTardio, Ausencias, Hablador")

    atributo = input("\nAtributo a buscar: ").strip()
    valor = input("Valor a buscar: ").strip()

    print("\nTipo de comparación:")
    print("1. Igual (=)")
    print("2. Mayor que (>)")
    print("3. Menor que (<)")

    opcion_comp = input("Selecciona tipo (1-3): ").strip()

    comparacion = "equal"
    if opcion_comp == "2":
        comparacion = "greater"
        try:
            valor = float(valor)
        except ValueError:
            print("❌ Error: El valor debe ser numérico para comparaciones > o <")
            return
    elif opcion_comp == "3":
        comparacion = "less"
        try:
            valor = float(valor)
        except ValueError:
            print("❌ Error: El valor debe ser numérico para comparaciones > o <")
            return

    resultados = manager.search_villains_by_attribute(atributo, valor, comparacion)

    print(f"\n--- RESULTADOS DE BÚSQUEDA ---")
    print(f"Se encontraron {len(resultados)} villano(s):\n")

    if resultados:
        for villain in resultados:
            print(f"  {villain}")
    else:
        print("  No se encontraron villanos con esos criterios")


def consultar_edad(manager):
    print("\n--- CONSULTAR EDAD DE PERSONAJE ---")

    try:
        char_id = int(input("Ingresa el ID del personaje: ").strip())

        personaje = manager.get_character_by_id(char_id)

        if personaje:
            edad = personaje.calculate_age()
            print(f"\n📋 Información del personaje:")
            print(f"  Nombre: {personaje.name} {personaje.last_name}")
            print(f"  ID: {personaje.id}")
            print(f"  Fecha de nacimiento: {personaje.birth_date}")
            print(f"  Edad: {edad} años")
            print(f"  Puntuación: {personaje.points:.2f}")
        else:
            print(f"❌ No se encontró ningún personaje con ID {char_id}")

    except ValueError:
        print("❌ Error: El ID debe ser un número entero")
    except Exception as e:
        print(f"❌ Error: {e}")


def emparejar_personajes(manager):
    print("\n--- EMPAREJAMIENTO ALEATORIO ---")

    pairing = manager.pair_random_characters()

    if "error" in pairing:
        print(f"❌ {pairing['error']}")
        return

    hero = pairing["hero"]
    villain = pairing["villain"]

    print("\n⚔️  ENFRENTAMIENTO ⚔️")
    print(f"\n🦸 HÉROE: {hero.name} {hero.last_name}")
    print(f"   Puntuación: {pairing['hero_score']:.2f}")
    print(f"   Edad: {hero.calculate_age()} años")

    print(f"\n   VS")

    print(f"\n😈 VILLANO: {villain.name} {villain.last_name}")
    print(f"   Puntuación: {pairing['villain_score']:.2f}")
    print(f"   Edad: {villain.calculate_age()} años")

    print(f"\n📊 ANÁLISIS DEL ENFRENTAMIENTO:")
    print(f"   Diferencia de puntuación: {pairing['score_difference']:.2f}")
    print(f"   Evaluación: {pairing['evaluation']}")
    print(f"   ¿Equilibrado?: {'✓ Sí' if pairing['is_balanced'] else '✗ No'}")
    print(
        f"   ¿Alta desviación?: {'✓ Sí' if pairing['has_high_deviation'] else '✗ No'}"
    )


def ver_estadisticas(manager):
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")

    stats = manager.get_statistics()

    print(f"\n📊 Resumen General:")
    print(f"   Total de Héroes: {stats['total_heroes']}")
    print(f"   Total de Villanos: {stats['total_villains']}")
    print(f"   Total de Personajes: {stats['total_characters']}")
    print(f"\n📈 Puntuaciones Promedio:")
    print(f"   Héroes: {stats['average_hero_score']:.2f}")
    print(f"   Villanos: {stats['average_villain_score']:.2f}")


def main():
    print("\n🎮 Iniciando Sistema de Gestión de Héroes y Villanos...")

    # Crear instancia del gestor de personajes
    manager = GestorPersonajes()

    # Diccionario de opciones del menú
    opciones = {
        "1": crear_heroe,
        "2": crear_villano,
        "3": listar_heroes,
        "4": listar_villanos,
        "5": buscar_heroe,
        "6": buscar_villano,
        "7": consultar_edad,
        "8": emparejar_personajes,
        "9": ver_estadisticas,
    }

    while True:
        try:
            mostrar_menu()
            opcion = input("\nSelecciona una opción (0-9): ").strip()

            if opcion == "0":
                print("\n👋 Saliendo del sistema...")
                print(
                    "📝 Revisa 'heroes_villains.log' para el registro completo de operaciones."
                )
                logging.info("Sistema cerrado por el usuario")
                break

            if opcion in opciones:
                opciones[opcion](manager)
            else:
                print(
                    "\n❌ Opción no válida. Por favor, selecciona un número del 0 al 9."
                )

            input("\nPresiona ENTER para continuar...")

        except KeyboardInterrupt:
            print("\n\n👋 Saliendo del sistema...")
            logging.info("Sistema cerrado con Ctrl+C")
            break
        except Exception as e:
            logging.error(f"Error en el menú principal: {e}")
            print(f"\n❌ Error inesperado: {e}")
            input("\nPresiona ENTER para continuar...")


main()
