import json #Importar JSON

def abrirArchivo():  # Define una función para abrir el archivo JSON
    with open('info.json','r') as openfile: # Abre el archivo en modo lectura
        return json.load(openfile) # Carga los datos del archivo JSON y los devuelve

def guardarArchivo(miData): # Define una función para guardar datos en el archivo JSON
    with open("info.json","w") as outfile: # Abre el archivo en modo escritura
        json.dump(miData,outfile) # Escribe los datos en el archivo JSON

def mostrarEstudiantes(estudiantes): # Define una función para mostrar los datos de los estudiantes
    for estudiante in estudiantes: # Itera sobre cada estudiante en la lista de estudiantes
        print("################") # Imprime un separador
        print("ID:", estudiante["id"]) # Imprime el ID del estudiante
        print("Nombre:", estudiante["nombre"]) # Imprime el nombre del estudiante
        print("Apellido:", estudiante["apellido"]) # Imprime el apellido del estudiante
        print("Edad:", estudiante["edad"]) # Imprime la edad del estudiante
        print("Fecha de Nacimiento (DD-MM-AAAA):", estudiante["fechaNacimiento"]) # Imprime la fecha de nacimiento del estudiante
        print("Cédula:", estudiante["cedula"]) # Imprime la cédula del estudiante
        print("E-mail:", estudiante["email"]) # Imprime el email del estudiante
        print("GitHub:", estudiante["github"]) # Imprime el GitHub del estudiante
        print("################\n") # Imprime un separador

def modificarEstudiante(estudiantes): # Define una función para modificar los datos de un estudiante
    mostrarEstudiantes(estudiantes) # Muestra los datos de los estudiantes
    estudiante_id = int(input("¿Cuál es el ID del estudiante que deseas modificar? ")) # Solicita al usuario el ID del estudiante a modificar
    for estudiante in estudiantes: # Itera sobre cada estudiante en la lista de estudiantes
        if estudiante["id"] == estudiante_id: # Comprueba si el ID del estudiante coincide con el proporcionado por el usuario
            print("Datos del estudiante:")  # Imprime un mensaje
            print("1. Nombre")
            print("2. Apellido")
            print("3. Edad")
            print("4. Fecha de Nacimiento")
            print("5. Cédula")
            print("6. E-mail")
            print("7. GitHub")
            opcion = int(input("Ingresa el dato que deseas modificar ")) # Solicita al usuario la opción de qué dato modificar
            nuevo_valor = input("Ingresa el nuevo valor: ") # Solicita al usuario el nuevo valor
            if opcion == 1:
                estudiante["nombre"] = nuevo_valor # Modifica el nombre del estudiante
            elif opcion == 2:
                estudiante["apellido"] = nuevo_valor
            elif opcion == 3:
                estudiante["edad"] = nuevo_valor
            elif opcion == 4:
                estudiante["fechaNacimiento"] = nuevo_valor
            elif opcion == 5:
                estudiante["cedula"] = nuevo_valor
            elif opcion == 6:
                estudiante["email"] = nuevo_valor
            elif opcion == 7:
                estudiante["github"] = nuevo_valor
    guardarArchivo(miInfo)

def crearEstudiante(estudiantes): # Define una función para crear un nuevo estudiante
    nuevo_estudiante = {} # Crea un diccionario para el nuevo estudiante
    nuevo_estudiante["id"] = len(estudiantes) + 1 # Asigna un nuevo ID al estudiante
    nuevo_estudiante["nombre"] = input("Ingresa el nombre del nuevo estudiante: ") # Solicita al usuario el nombre del nuevo estudiante
    nuevo_estudiante["apellido"] = input("Ingresa el apellido del nuevo estudiante: ")
    nuevo_estudiante["edad"] = input("Ingresa la edad del nuevo estudiante: ")
    nuevo_estudiante["fechaNacimiento"] = input("Ingresa la fecha de nacimiento del nuevo estudiante (DD-MM-AAAA): ")
    nuevo_estudiante["cedula"] = input("Ingresa la cédula del nuevo estudiante: ")
    nuevo_estudiante["email"] = input("Ingresa el email del nuevo estudiante: ")
    nuevo_estudiante["github"] = input("Ingresa el GitHub del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante) # Agrega el nuevo estudiante a la lista de estudiantes
    guardarArchivo(miInfo) # Guarda los cambios en el archivo JSON
 
def eliminarEstudiante(estudiantes):
    mostrarEstudiantes(estudiantes) # Muestra los datos de los estudiantes
    estudiante_id = int(input("¿Cuál es el ID del estudiante que deseas eliminar? ")) # Solicita al usuario el ID del estudiante a eliminar
    for estudiante in estudiantes: # Itera sobre cada estudiante en la lista de estudiantes
        if estudiante["id"] == estudiante_id: # Comprueba si el ID del estudiante coincide con el proporcionado por el usuario
            estudiantes.remove(estudiante) # Elimina el estudiante de la lista de estudiantes
            print("Estudiante eliminado exitosamente.")
            break
    else:
        print("¡Estudiante no encontrado!")
    guardarArchivo(miInfo)

# Menú principal
print("################")
print("## Menú ##")
print("################\n")

print("Hola! Escoge una de las opciones:")
print("1. Revisar estudiantes")
print("2. Modificar estudiante")
print("3. Crear estudiante")
print("4. Eliminar estudiante")
print("5. Finalizar")

opcion = int(input("Ingresa tu opción: "))

if opcion == 1:
    miInfo = abrirArchivo() # Abre el archivo JSON y carga los datos
    mostrarEstudiantes(miInfo[0]["estudiantes"]) # Muestra los datos de los estudiantes
elif opcion == 2:
    miInfo = abrirArchivo()
    modificarEstudiante(miInfo[0]["estudiantes"])
elif opcion == 3:
    miInfo = abrirArchivo()
    crearEstudiante(miInfo[0]["estudiantes"])
elif opcion == 4:
    miInfo = abrirArchivo()
    eliminarEstudiante(miInfo[0]["estudiantes"])
elif opcion == 5:
    print("¡Hasta luego!")
    # exit()

