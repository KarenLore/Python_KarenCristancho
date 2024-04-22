def posicion(nums, target):
#Recorremos la lista de números
    for i in range (len(nums)):
#Comparamos cada número con el objetivo
        if nums[i] >= target: #Si se encuentra un número mayor o igual al objetivo, devolvemos su indice.
            return i
    return len(nums) #Si recorremos toda la lista sin encontrar un número mayor, devolvemos la longitud de la lista

#Permite al usuario ingresar los números y el objetivo
numeros = list(map(int, input("Ingresa los números: ").split(",")))
objetivo = int(input("Ingrese el objetivo: "))

#Llamar la función con los números ingresados y mostramos el resultado
print("La posición del objetivo es: ", posicion(numeros, objetivo))  
