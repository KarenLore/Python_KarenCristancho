# Definición de la lista de frutas
frutas = [('banana', 0.45, 6), ('jackfruit', 4.55, 2), ('kiwi', 0.15, 23)]

#a
# Convertir los nombres de las frutas a mayúsculas
frutas_mayusculas = [fruta[0].upper() for fruta in frutas]
print(frutas_mayusculas)

#b
# Mostrar solo las frutas cuyo precio es inferior a 0.50
frutas_baratas = [fruta[0] for fruta in frutas if fruta[1] < 0.50]
print(frutas_baratas)

#c
# Encontrar la fruta que tiene la mayor cantidad disponible
# key=lambda x: x[2] especifica que se debe comparar la cantidad (el tercer elemento de cada tupla)
fruta_maxima = max(frutas, key=lambda x: x[2])
print(fruta_maxima)

#d
# Ordenar las frutas de mayor a menor valor en stock (cantidad * precio)
# key=lambda x: x[1] * x[2] especifica que se debe calcular el valor de la fruta en stock multiplicando el precio por la cantidad
# reverse=True especifica que se debe ordenar en orden descendente (del más caro al más barato)
frutas_ordenadas = sorted(frutas, key=lambda x: x[1] * x[2], reverse=True)
print(frutas_ordenadas)
