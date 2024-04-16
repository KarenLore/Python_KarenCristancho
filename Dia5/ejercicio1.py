def resolver():
    # T es el número de casos de prueba
    T = int(input())
    # Iteramos sobre cada caso de prueba
    for t in range(1, T+1):
        # n es el número de elementos en la lista, k es el número con el que se realizará la operación módulo
        n, k = map(int, input().split())
        # a es la lista de números
        a = list(map(int, input().split()))
        # count es el contador para el número de pares que cumplen la condición
        count = 0
        # Iteramos sobre cada elemento en la lista
        for i in range(n):
            # Comparamos el elemento actual con los elementos siguientes en la lista
            for j in range(i+1, n):  
                # Verificamos si el primer número es menor o igual al segundo y si la suma de los dos números es divisible por k
                if a[i] <= a[j] and (a[i] + a[j]) % k == 0:
                    # Incrementamos el contador
                    count += 1
        # Imprimimos el número de caso y el contador
        print(f'Case {t}: {count+1}')

# Llamamos a la función solve
resolver()

#map convierte los elementos ingresados por el usuario en una lista de enteros
#split divide la cadena de texto en partes más pequeñas.
#f incluye el valor de las variables dentro de una cadena de texto
#% devuelve el residuo de la división de dos números.



