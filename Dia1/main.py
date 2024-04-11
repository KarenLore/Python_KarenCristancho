#---------------------------
#-----DIA 1 SHEET PYTHON----
#---------------------------

#Imprimir Hola mundo
print("¡Hola Mundo!")

#Datos primitivos

#Número
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))

#Ingresa por teclado la información (input)
print("Ingresa tu nombre")
nombre = input()
print("Tu nombre es", nombre)

#Conversión de tipos de variables (Convertir string a un numero, numero a booleano)
numero = 10 
print(type(numero))
numero = str(numero)
print(type(numero))
numero = float(numero)
print(type(numero))
numero = bool(numero)
print(type(numero))
numero = int(numero)

#Bucles For y While
#Bucle for: Imprime los número del 0 al 4
for i in range(5):
    print(i)
#Bucle while: Imprime los números del 0 al 4
i=0
while i < 5:
    i+=1

#Funciones (4 Tipos)
#Funcion sin parámetros ni valor de retorno
def saludar():
    print("¡Hello Word!")
#Llamada a la función
    saludar()

#Función con parámetro pero sin valor de retorno:
def saludar_nombre(nombre):
    print("¡Hola Mundo,", nombre, "!")
#Llamada a la función
    saludar_nombre()

#Función sin parámetros pero con valor de retorno:
def obtener_numero():
    return 42
#Llamada a la función
numero = obtener_numero()
print("El número es: ", numero)

#Función con parámetro y con valor de retorno:
def sumar(a, b):
    return a + b
resultado = sumar(3,5)
print("La suma es: ", resultado)

#Desarrollado por Karen Cristancho