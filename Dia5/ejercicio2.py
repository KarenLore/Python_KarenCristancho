while True:
    # Leer el número de tipos de monedas y el número de mesas a diseñar
    n, t = map(int, input().split())

    # Verificar si es el caso de salida
    if n == 0 and t == 0:
        break

    # Leer los espesores de las monedas
    monedas = [int(input()) for _ in range(n)]

    # Leer las alturas de las mesas
    alturas = [int(input()) for _ in range(t)]

    # Para cada mesa, encontrar la longitud más cercana superior e inferior
    for altura in alturas:
        mayor_longitud = max(monedas) * 4
        menor_longitud = min(monedas) * 4
        for moneda in monedas:
            # Calcular el múltiplo más cercano a la altura de la mesa
            multiplo = altura // moneda
            # Actualizar la mayor longitud si es necesario
            mayor_longitud = min(mayor_longitud, moneda * multiplo if moneda * multiplo >= altura else moneda * (multiplo + 1))
            # Actualizar la menor longitud si es necesario
            menor_longitud = max(menor_longitud, moneda * multiplo if moneda * multiplo <= altura else moneda * (multiplo - 1))
        # Imprimir las longitudes mayor y menor para la mesa actual
        print(mayor_longitud, menor_longitud)
        
#map convierte los elementos ingresados por el usuario en una lista de enteros
#split divide la cadena de texto en partes más pequeñas.