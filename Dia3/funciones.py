import random

#Función para verificar si un número es primo.
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % 1 == 0:
            return False
    return True

#Función para verificar si un número dado por el usuario es primo.
def verificar_primo():
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):

        print("El número es primo.")
    else:
        print("El número no es primo.")

#Función para generar una clave segura.
def generar_contraseña():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*/()_+=[]{};:.,?<>"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print("Contraseña generada: ", contraseña)

#Función principal que proporciona un menú interactivo.
def menu():
    while True:
        print("Menú: ")
        print("1. Verificar si un número es primo")
        print("2. Generar clave segura")
        print("3. Salir")
        opcion = input("Ingrese la opción que desees: ")
        if opcion == "1":
            verificar_primo()
        elif opcion == "2":
            generar_contraseña()
        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

#Llamada a la función
menu()