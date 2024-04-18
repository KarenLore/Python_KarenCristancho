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
    for id, producto in productos.items(): #items() puedes recorrer un diccionario y acceder a cada par clave-valor (es decir, producto por producto en este contexto).
        print(f"ID: {id}\nNombre: {producto['Nombre']}\nPrecio:${producto['Precio']}")
        print()

# Función para agregar productos al carrito de compras
def agregar_al_carrito(carrito):
    id_producto = input("Ingrese el ID del producto que desea agregar al carrito: ")
    cantidad = int(input("Ingrese la cantidad deseada del producto: "))
    
    if id_producto in productos:
        if cantidad <= productos[id_producto]["Cantidad disponible"]:
            carrito[id_producto] = carrito.get(id_producto) + cantidad #get(), puedes acceder a los valores asociados a las claves que ya están definidas en el diccionario. Si la clave está presente en el diccionario
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

#Llamar la función menú
menu()

#Diccionario de Productos: Define un diccionario que almacena información sobre los productos disponibles, incluyendo el nombre, precio y cantidad disponible.
#Función para Mostrar el Catálogo de Productos: Esta función imprime el catálogo de productos con sus respectivos ID, nombres y precios.
#Función para Agregar Productos al Carrito: Esta función permite al usuario agregar productos al carrito de compras, solicitando el ID del producto y la cantidad deseada.
#Función para Mostrar el Contenido del Carrito de Compras: Esta función muestra el contenido del carrito de compras, incluyendo los productos agregados y sus cantidades correspondientes.
#Función para Calcular el Total de la Compra:  Esta función calcula el total de la compra sumando el precio de cada producto multiplicado por su cantidad en el carrito.
#Función para el Menú Principal: Esta función representa el menú principal del programa, donde el usuario puede realizar varias acciones, como agregar productos al carrito, ver el contenido del carrito, calcular el total de la compra, finalizar la compra o salir del programa.

            


       
