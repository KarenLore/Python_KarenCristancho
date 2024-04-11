import random
def Numero_Secreto():
    #Generar un número secreto aleatorio entre 1 y 100
    Numero_Secreto = random.randint(1, 100)
    intentos_realizados = 0

    print("Bienvenido al juego de adivinar el número secreto")
    print("El número secreto está entre 1 y 100. ¡Buena Suerte!")

    #Bucle principal para permitir que el usuario adivine el número
    while True:
        #Solicitar al usuario que ingrese su suposición
        intento = int(input("\nIngrese su suposición"))
        intentos_realizados += 1

        #Comprobar si el intento del usuario es menor, mayor o igual al número
        if intento < Numero_Secreto:
            print("El número secreto es mayor. Vuelve a intentarlo.")
        elif intento > Numero_Secreto:
            print("El número secreto es menor. Vuelve a intentarlo.")
        else:
            #Si el intento es igual al número secreto, el usuario ha adivinado
            print(f"Felicidades, ¡Has adivinado el número secreto {Numero_Secreto} en {intentos_realizados}!")
            break

#Llamada a la función Numero_Secreto
Numero_Secreto()

