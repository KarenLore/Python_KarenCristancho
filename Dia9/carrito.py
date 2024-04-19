carrito = [] #Lista vacía
cantidad=int(input(f"Ingrese la cantidad de productos que deseas agregar: ")) #Cantidad de  productos que desea agregar al carrito
print("")
#Agregar artículos al carrito
for i in range(cantidad):
    nombre= input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese el precio del producto: {nombre} "))
    precio = int(input(f"Ingrese la cantidad del producto: {nombre} "))
    carrito.append((nombre,cantidad,precio)) #Agregar contenido a la lista vacía
    print("Producto agregado al carrito")
    print("")

print("==========Productos agregados al carrito===========\n ")
contador = 0
for i in carrito: #Imprime la lista de los productos desde la posición 0 hasta la 2
    print("Nombre ", i[0])
    print("Precio ", i[1])
    print("Cantidad ", i[2])
    print("")
contador = contador +1

