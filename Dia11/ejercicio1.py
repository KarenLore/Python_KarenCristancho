import json

#Abrir el archivo JSON y cargar los datos en una lista
with open('large-file.json', encoding="utf-8") as file:
    lista = json.load(file)

#Imprimir el tipo de dato de la lista cargada
print(lista)
#Bucle principal para mostrar el menú y manejar las opciones del usuario
while True:
    #Mostrar el menú
    print("\n##### MENÚ #####")
    #Opciones del menú
    print("1. Revisar evento\n2. Crear evento\n3. Actualizar eventos\n4. Eliminar evento\n5. Salir")
    #Solicitar que se ingrese una opción
    opcion= input("Ingrese opción: ")
    #Utilizar la estructura match para manejar las opciones
    crearEvents=[]
    match opcion:
        case "1":
            #Recorrer la lista de eventos e imprimir cada evento con su número
            for i, evento in enumerate (lista, 1):
                #Imprimir el tipo y el ID del evento
                print(f"{i}. ID:{evento["id"]} - Type: {evento["type"]} - Actor{evento["actor"]} - Repo{evento["repo"]} - Login{evento["login"]} - Avatar_URL{evento["avatar_url"]}")
                print("")

        case "2":
            # Solicitar al usuario que ingrese el tipo y el ID del nuevo evento
            nuevo_E = input("Ingrese el tipo de evento: ")
            nuevo_id = input("Ingrese el ID del evento: ")
            # Crear un diccionario para representar el nuevo evento
            nuevo_evento_Actor = {"type": nuevo_E, "id": nuevo_id}
            nuevo_evento_Repo = {"type": nuevo_E, "id": nuevo_id}
            # Agregar el nuevo evento a la lista de eventos
            lista.append(nuevo_evento_Actor)
            lista.append(nuevo_evento_Repo)
            print("Evento creado correctamente.")

        case "3":
            # Solicitar al usuario que ingrese el número del evento que desea actualizar
            evento_a_actualizar = int(input("Ingrese el número del evento que desea actualizar: ")) - 1
             # Solicitar al usuario que ingrese el nuevo tipo y el nuevo ID del evento
            lista[evento_a_actualizar]["type"] = input("Ingrese el nuevo tipo de evento: ")
            lista[evento_a_actualizar]["id"] = input("Ingrese el nuevo ID del evento: ")
            print("Evento actualizado correctamente.")

        case "4":
            # Solicitar al usuario que ingrese el número del evento que desea eliminar
            evento_a_eliminar = int(input("Ingrese el número del evento que desea eliminar: ")) - 1
            # Eliminar el evento seleccionado de la lista de eventos
            lista.pop(evento_a_eliminar)
            print("Evento eliminado correctamente.")

        case "5":
            print("Gracias por usar el programa.")
            break

with open("eventos.json","w") as outfile:
    json.dump(lista,outfile)
#Pop es para eliminar
# with open(...) as file: Abre el archivo 'large-file.json' en modo de lectura con la codificación utf-8 y lo asigna a la variable 'file'. La instrucción 'with' asegura que el archivo se cierre automáticamente después de que se complete el bloque de código dentro de la declaración 'with'.
# lista = json.load(file): Utiliza la función load del módulo json para cargar los datos del archivo JSON contenido en 'file' en una lista llamada 'lista'. Esto convierte el contenido del archivo JSON en una estructura de datos Python.