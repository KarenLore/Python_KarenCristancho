# Un número primo es aquel que solo es divisible por 1 y por sí mismo.
import random #Es como una bibloteca de funciones relacionadas con la generación de números aleatorios.

#Función para verificar si un número es primo.
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % 1 == 0: #Para verificar si el número es divisible por 1.
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
#longitud cantidad de caracteres que el usuario desea qye tenga la contraseña
#random.choice selecciona aleatoriamente de la cadena de caracteres
#''.join une los caracteres aleatorios en una sola cadena sin ningún separador
def generar_contraseña():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*/()_+=[]{};:.,?<>"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    print("Contraseña generada: ", contraseña)

#Función principal que proporciona un menú interactivo.
def menu():
    print("¡Biendenidos al programa!")
    print("Este programa tiene dos funciones:")
    print("-Determinar si el número dado por el usuario es primo.")
    print("El propósito del aplicativo es proporcionas una herramienta en el que el usuario pueda verificar si un número es primo o no.")
    print("-Generar contraseñas seguras.")
    print("El programa ofrece un generador de contraseñas seguras que permite a los usuarios crear una contraseña de longitud variable y con diferentes tipos de caracteres.")

    while True:
        print("Menú: ")
        print("1. Verificar si un número es primo")
        print("2. Crear contraseña")
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