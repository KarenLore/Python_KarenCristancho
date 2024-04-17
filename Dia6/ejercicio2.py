def suma(nums, tagert):
    num_indices ={} # Creamos un diccionario vacío para almacenar números y sus índices.
    for i, num in enumerate(nums): # Recorremos la lista nums junto con sus índices.
        if tagert - num in num_indices: # Verificamos si el complemento de num está en el diccionario.
            return[num_indices[tagert - num], i] # Si está, retornamos los índices de los dos números.
        num_indices[num]=i # Almacenamos el número actual junto con su índice en el diccionario.

#Leer entrada del usuario
nums = list(map(int, input()))
tagert = int(input())

#Llamar la función e imprimit resultado
print(suma(nums, tagert))

#i representa el número actual en la lista nums
#enumerate permite recorrer la lista
#{} crea un diccionario vacío
#El indice es el número entero que representa la posición del elemento.