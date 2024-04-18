# Catálogo de productos con identificadores únicos y precios
productos = {
    "001":{"Nombre": "Camiseta", "Precio":30000, "Cantidad disponible":10},
    "002":{"Nombre": "Pantalon", "Precio":50000, "Cantidad disponible":20},
    "003":{"Nombre": "Zapatos", "Precio":100000, "Cantidad disponible":15},
    "004":{"Nombre": "Busos", "Precio":40000, "Cantidad disponible":5}
}

# Función para mostrar el catálogo de productos
def mostrar_catálago():
    print("Catálago de productos:")
    for id, producto in productos.items():
        print(f"ID: {id}\nNombre: {producto['Nombre']}\nPrecio:${producto['Precio']}")
        print()

# Función para agregar productos al carrito de compras
def agregar_al_carrito(carrito):
    id_producto = input("Ingrese el ID del producto que desea agregar al carrito: ")
    cantidad = int(input("Ingrese la cantidad deseada del producto: "))
    
    if id_producto in productos:
        if cantidad <= productos[id_producto]["Cantidad disponible"]:
            carrito[id_producto] = carrito.get(id_producto, 0) + cantidad
            print("Producto agregado al carrito.")
        else:
            print("La cantidad ingresada excede la cantidad disponible.")
    else:
        print("Producto no encontrado.")

# Función para mostrar el contenido del carrito de compras
def mostrar_carrito(carrito):
    print("Contenido del carrito: ")
    for id, cantidad in carrito.items():
        nombre = productos[id]['Nombre']
        precio = productos[id]['Precio']
        subtotal = precio * cantidad
        print(f"Producto:{nombre}, Cantidad:{cantidad}, Subtotal:${subtotal}")
    else:
        print("El carrito está vacío.")

# Función para calcular el total de la compra
def calcular_total(carrito):
    total = 0
    for id, cantidad in carrito.items():
        precio = productos[id]['Precio']
        subtotal = precio * cantidad
        total += subtotal
    print(f"Total de la compra: ${total}")

def menu():
    carrito = {}
    print("Bienvenido a nuestra tienda virtual.")
    mostrar_catálago()
    definir=True
    while definir:
        print("===========Menú==========")
        print("1. Agregar productos al carrito.")
        print("2. Ver contenido del carrito.")
        print("3. Calcular total de la compra.")
        print("4. Finalizar compra.")
        print("5. Salir del simulador.")
        opcion = input("Ingrese la opción que desees: ")
        if opcion == "1":
            agregar_al_carrito(carrito)
        elif opcion == "2":
            mostrar_carrito(carrito)
        elif opcion == "3":
            calcular_total(carrito)
        elif opcion == "4":
            print("Compra finalizada. ¡Gracias por su compra!")
            print("deseas continuar con el programa")
            respuesta=input()
            if respuesta=="si":
                definir=True
            else:
                print("Gracias por utilizar nuestra tienda virtual.")
                definir=False

        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intentelo de nuevo.")

menu()
            


       
