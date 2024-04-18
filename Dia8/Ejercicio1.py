def menu():
    print("Bienvenido a periodico PYTimes")
    mostrar_catálago()
while True:
    print("===========Menú==========")
    print("1. Suscribirse al periodico.")
    print("2. Sucribir amigo al periodico.")

    periodicos = {
        "1":{"Nombre": "El universal", "Precio":50000},
        "2":{"Nombre": "La opinión", "Precio":50000},
        "3":{"Nombre": "El economista", "Precio":50000},
        "4":{"Nombre": "La jornada", "Precio":50000}
        }
    # Función para mostrar el catálogo de productos
    def mostrar_catálago():
        print("Catálago de productos:")
        for id, periodicos in periodicos.items(): #items() puedes recorrer un diccionario y acceder a cada par clave-valor (es decir, producto por producto en este contexto).
            print(f"\nNombre: {periodicos['Nombre']}\nPrecio:${periodicos['Precio']}")
            print()
    

    def suscripcion():
        nombre = str(input("Ingresa tu nombre: "))
        precio = 50
        saldo=int(input("Ingresa tu deposito: "))
        print(f"Nombre:{nombre} El valor de la suscripción es:{precio}")
        print(f"Deposito:{saldo}")
    suscripcion()

    vuelve= int(input("Desea suscribirse (si/no)"))
    if vuelve == "si":
        print("Ingrese su deposito para poder realizar la suscripción: {saldo}")

