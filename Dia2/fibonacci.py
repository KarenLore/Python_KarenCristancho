while True:
    print("Bienvenido al programa de la Secuencia de Fibonacci ")
    print("La secuencia de fibonacci trata de una serie infinita de números naturales que empieza con un 0 y un 1 y continúa añadiendo números el cual sería la suma de los dos números anteriores")

#Solicita al usuario que ingrese un número entero
    n=int(input("Ingrese un número entero: "))

#Inicializa las variables para generar la secuencia Fibonacci
    a, b = 0, 1
    c = 1

#Mientras no se haya alcanzado el término n de la secuencia
    while c <= n:
    #Si es un índice impar en la secuencia
        if c % 2 == 1:
        #Imprime el número de Fibonacci actual
            print(a, end=", ")
        #Actualiza el valor de "a" sumando "b"
            a += b
        else:
        #Si es un índice par en la secuencia
        #Imprime el número de Fibonacci actual
            print(b, end=", ")
        #Actualizar el valor "b" sumando "a"
            b+= a
    #Incrementar el contador
        c+= 1

#Pregunta al usuario si desea continuar
    continuar = input("\n¿Desea continuar? (s/n): ").lower()
#Si la respuesta no es "s" sale del bucle y finaliza el programa
    if continuar != "s":
        print("¡Hasta luego!")
        break
