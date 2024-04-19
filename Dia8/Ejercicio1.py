class Usuario:
    def __init__(self, nombre, precio_suscripcion=50):
        # Método para inicializar un objeto Usuario con nombre y precio de suscripción
        self.nombre = nombre
        self.precio_suscripcion = precio_suscripcion
        self.suscripciones = []  # Inicializa la lista de suscripciones del usuario
        self.saldo = 0  # Inicializa el saldo del usuario

    def recargar_saldo(self, cantidad):
        # Método para recargar el saldo del usuario
        self.saldo += cantidad  # Añade la cantidad al saldo del usuario
        print("¡Saldo recargado con éxito! Saldo actual:", self.saldo)  # Imprime el saldo actual del usuario

    def suscribirse(self, año):
        # Método para que un usuario se suscriba a un año específico
        if self.saldo >= self.precio_suscripcion:  # Verifica si el usuario tiene suficiente saldo
            self.saldo -= self.precio_suscripcion  # Resta el precio de la suscripción al saldo del usuario
            self.suscripciones.append(año)  # Agrega el año de suscripción a la lista de suscripciones del usuario
            print("¡Te has suscrito con éxito para el año", año, "!")  # Imprime un mensaje de éxito
        else:
            print("¡No tienes suficiente dinero en tu cuenta! Saldo actual:", self.saldo)  # Imprime un mensaje de error

    def mostrar_suscripciones(self):
        # Método para mostrar las suscripciones del usuario
        if self.suscripciones:  # Verifica si el usuario tiene suscripciones
            print("Suscripciones de", self.nombre + ":")  # Imprime el nombre del usuario
            for suscripcion in self.suscripciones:  # Itera sobre las suscripciones del usuario
                print(suscripcion)  # Imprime cada suscripción
        else:
            print("No tienes suscripciones.")  # Imprime un mensaje si el usuario no tiene suscripciones

def Menu():
    # Función principal que ejecuta el menú y las acciones correspondientes
    nombre_usuario = input("Ingresa tu nombre: ")  # Solicita al usuario que ingrese su nombre
    usuario = Usuario(nombre_usuario)  # Crea un usuario con el nombre proporcionado
    amigo = Usuario("Amigo")  # Crea otro usuario llamado "Amigo"

    while True:  # Ciclo para mostrar el menú hasta que el usuario elija salir
        print("Bienvenido a la tienda de periódicos PYTimes")  # Mensaje de bienvenida
        print("1. Recargar saldo\n2. Suscribirme\n3. Comprar suscripción como regalo\n4. Mostrar suscripciones\n5. Salir")  # Opciones del menú
        opcion = input("Elige una opción: ")  # Solicita al usuario que elija una opción del menú

        if opcion == "1":
            cantidad = int(input("Ingresa la cantidad a recargar: "))  # Solicita al usuario que ingrese la cantidad a recargar
            usuario.recargar_saldo(cantidad)  # Llama al método para recargar el saldo del usuario
        elif opcion == "2":
            año = input("Ingresa el año para la suscripción: ")  # Solicita al usuario que ingrese el año de la suscripción
            usuario.suscribirse(año)  # Llama al método para suscribir al usuario
        elif opcion == "3":
            año = input("Ingresa el año para la suscripción: ")  # Solicita al usuario que ingrese el año de la suscripción
            usuario.comprar_suscripcion_regalo(amigo, año)  # Llama al método para comprar una suscripción como regalo
        elif opcion == "4":
            usuario.mostrar_suscripciones()  # Llama al método para mostrar las suscripciones del usuario
            amigo.mostrar_suscripciones()  # Llama al método para mostrar las suscripciones del "amigo"
        elif opcion == "5":
            print("Saliendo del programa...")  # Mensaje de despedida
            break  # Sale del ciclo y termina el programa
        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Mensaje de error si el usuario elige una opción inválida

Menu()  # Llama a la función principal para iniciar el programa
