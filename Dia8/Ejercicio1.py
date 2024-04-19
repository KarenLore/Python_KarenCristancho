def crear_usuario(nombre, precio_suscripcion=50):
    return {"nombre": nombre, "precio_suscripcion": precio_suscripcion, "suscripciones": [], "saldo": 0}

def agregar_suscripcion(usuario, año):
    usuario["suscripciones"].append(año)

def suscribirse(usuario, año):
    if usuario["saldo"] >= usuario["precio_suscripcion"]:
        usuario["saldo"] -= usuario["precio_suscripcion"]
        agregar_suscripcion(usuario, año)
        print("¡Te has suscrito con éxito para el año", año, "!")
    else:
        print("¡No tienes suficiente dinero en tu cuenta! Saldo actual:", usuario["saldo"])

def comprar_suscripcion_regalo(usuario, otro_usuario, año):
    if usuario["saldo"] >= otro_usuario["precio_suscripcion"]:
        usuario["saldo"] -= otro_usuario["precio_suscripcion"]
        agregar_suscripcion(otro_usuario, año)
        print("¡Suscripción comprada como regalo con éxito para", otro_usuario["nombre"], "para el año", año, "!")
    else:
        print("¡No tienes suficiente dinero en tu cuenta para comprar la suscripción como regalo! Saldo actual:", usuario["saldo"])

def recargar_saldo(usuario, cantidad):
    usuario["saldo"] += cantidad
    print("¡Saldo recargado con éxito! Saldo actual:", usuario["saldo"])

def mostrar_menu():
    print("1. Recargar saldo")
    print("2. Suscribirme")
    print("3. Comprar suscripción como regalo")
    print("4. Salir")

def obtener_opcion():
    opcion = input("Elige una opción: ")
    return opcion

def obtener_año():
    año = input("Ingresa el año para la suscripción: ")
    return año

def obtener_cantidad():
    cantidad = int(input("Ingresa la cantidad a recargar: "))
    return cantidad

def obtener_nombre_usuario():
    nombre = input("Ingresa tu nombre: ")
    return nombre

def Menu():
    nombre_usuario = obtener_nombre_usuario()
    usuario = crear_usuario(nombre_usuario)
    otro_usuario = crear_usuario("Amigo")

    while True:
        print("Bienvenido a tienda periodicos PYTimes")
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == "1":
            cantidad = obtener_cantidad()
            recargar_saldo(usuario, cantidad)
        elif opcion == "2":
            año = obtener_año()
            suscribirse(usuario, año)
        elif opcion == "3":
            año = obtener_año()
            comprar_suscripcion_regalo(usuario, otro_usuario, año)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

Menu()



