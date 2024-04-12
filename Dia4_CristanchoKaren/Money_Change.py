def minimo_numero_monedas(cambio):

    #Calcula el número de monedas 10 necesarias y actualiza el valor de cambio.
    num_monedas_10 = cambio // 10
    cambio %= 10

    #Calcula el número de monedas 5 necesarias y actualiza el valor de cambio.
    num_monedas_5 = cambio // 5
    cambio %= 5
    
    #Calcula el número de monedas 1 necesarias.
    num_monedas_1 = cambio // 1

    #Calcula el total de monedas necesarias.
    total_monedas= num_monedas_1 + num_monedas_5 + num_monedas_10

    #Devuelve el total de monedas y la cantidad de cada denominación.
    return total_monedas, num_monedas_1, num_monedas_5, num_monedas_10

#Solicita al usuario que ingrese el valor para el cambio deseado.
valor = int(input("Ingrese el valor para el cambio:"))

#Llama a la función para calcular el mínimo número de monedas.
total_monedas, monedas_1, monedas_5, monedas_10 = minimo_numero_monedas(valor)

#Imprime la cantidad de monedas necesarias para cada denominación y el total de monedas. 
print("Monedas de 1 necesarias: ", monedas_1)
print("Monedas de 5 necesarias: ", monedas_5)
print("Monedas de 10 necesarias: ", monedas_10)
print("El total de monedas es: ", total_monedas)

# % Para obtener el residuo de la de la división del valor del cambio actual entre 10.
# // Para realizar la división entera al calcular el número de monedas necesarias.
