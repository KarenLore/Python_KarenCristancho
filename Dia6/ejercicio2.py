def encontrar_indices_suma(nums,target):
    indices={} #Para crear un diccionario vacío para almacenar números y sus índices
    for i, num in enumerate(nums): # Recorrer la lista nums junto con sus indices
        complemento = target - num #Calcular el complemento necesario para alcanzar el objetivo
        if complemento in indices:#Verificar si el complemento esta en el diccionario
            return[indices[complemento],i] #Si esta, se retorna los índices de los números
        indices[num]=i #Almacenamos el número actual junto con su índice en el diccionario

#Leer entrada del usuario
nums = list(map(int, input().split()))
target = int(input())

#Llamar la función e imprimir resultado
print(encontrar_indices_suma(nums,target))

#i representa el número actual en la lista nums
#enumerate permite recorrer la lista
#{} crea un diccionario vacío
#El indice es el número entero que representa la posición del elemento. 
#-num calcula el complemento necesario para alcanzar el objetivo deseado cuando se suma con el número actual.
# 9-2 =7