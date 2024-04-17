productos = {
    "001":{"Nombre": "Camiseta", "Precio":30},
    "002":{"Nombre": "Pantalon", "Precio":50},
    "003":{"Nombre": "Zapatos", "Precio":100},
    "004":{"Nombre": "Busos", "Precio":40},
}

def mostrar_catálago():
    print("Catálago de productos:")
    for id, productos in productos.items():
        print(f"ID: {id}, Nombre:{productos['Nombre']}, Precio:${productos['Precio']}")

def agregar_al_carrito(carrito):
    id_producto = input("Ingrese el ID del producto que deseas agregar al carrito: ")
    cantidad = int(input("Ingrese la cantidad deseada del producto: "))
    if id_producto in productos:
        if cantidad > 0:
            


       
