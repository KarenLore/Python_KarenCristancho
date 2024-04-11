import random
def Numero_Secreto():
    #Generar un número secreto aleatorio entre 1 y 100
    Numero_Secreto = random.randint(1, 100)
    intentos_restantes = 10

    print("Bienvenido al juego de adivinar el número secreto")
    print ("Tienes un total de 10 intentos para lograr adivinar el número secreto")
    print("Después de cada intento, te diremos si el número secreto es mayor o menor que su suposición ¡Buena Suerte!")

    #Bucle principal para permitir que el usuario adivine el número
    while intentos_restantes > 0:
        #Solicitar al usuario que ingrese su suposición
        print(f"\nIntentos restantes: {intentos_restantes}")
        intento = int(input("Ingrese su suposición"))

        #Comprobar si el intento del usuario es menor, mayor o igual al número
        if intento < Numero_Secreto:
            print("El número secreto es mayor.")
        elif intento > Numero_Secreto:
            print("El número secreto es menor.")
        else:
            #Si el intento es igual al número secreto, el usuario ha adivinado
            print(f"Felicidades, ¡Has adivinado el número secreto {Numero_Secreto} en {10 - intentos_restantes + 1} intentos!")
            return 
        
        intentos_restantes -= 1
    print(f"\nLo siento, has agotado los 10 intentos. El numero secreto era: {Numero_Secreto()}")

#Llamado de la función
Numero_Secreto()
