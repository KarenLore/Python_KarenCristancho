# Leemos una línea de entrada que contiene números separados por espacios
# Tomamos los primeros 300 números ingresados para cumplir con el límite
# Convertimos cada número de cadena a entero y los almacenamos en una lista
nodos = list(map(int,input().split()[:300]))
# Eliminamos duplicados convirtiendo la lista en un conjunto y luego volviéndola a convertir en lista
# Ordenamos la lista resultante
repetidos = sorted(set(nodos))
#Imprimimos la lista de números sin duplicados y ordenada
print(repetidos)