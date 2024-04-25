# Importar el módulo json para manejar archivos JSON
import json

# Cargar los datos desde el archivo JSON 'large-file.json'
with open('large-file.json', encoding="utf-8") as file:
    lista = json.load(file)

# Definir listas vacías para cada tipo de evento
CreateEvent = []
PushEvent = []
WatchEvent = []
ReleaseEvent = []
PullRequestEvent = []
IssuesEvent = []
ForkEvent = []
GollumEvent = []
IssueCommentEvent = []
DeleteEvent = []
PullRequestReviewCommentEvent = []
CommitCommentEvent = []
MemberEvent = []
PublicEvent = []

# Función para crear un nuevo evento
def create_event():
    # Solicitar al usuario los detalles del nuevo evento
    event_type = input("¿Qué tipo de evento deseas crear? (CreateEvent, PushEvent, etc.): ")
    actor_id = input("Ingresa el ID del actor: ")
    actor_login = input("Ingresa el login del actor: ")
    actor_avatar_url = input("Ingresa la URL del avatar del actor: ")
    repo_id = input("Ingresa el ID del repositorio: ")
    repo_name = input("Ingresa el nombre del repositorio: ")
    is_public = input("¿Es público? (True/False): ")

    # Crear un diccionario que represente el nuevo evento
    event = {
        "event_type": event_type,
        "actor": {
            "id": actor_id,
            "login": actor_login,
            "avatar_url": actor_avatar_url
        },
        "repo": {
            "id": repo_id,
            "name": repo_name
        },
        "public": is_public
    }

    # Agregar el nuevo evento a la lista correspondiente según su tipo
    if event_type == "CreateEvent":
        CreateEvent.append(event)
    elif event_type == "PushEvent":
        PushEvent.append(event)
    elif event_type == "WatchEvent":
        WatchEvent.append(event)
    elif event_type == "ReleaseEvent":
        ReleaseEvent.append(event)
    elif event_type == "PullRequestEvent":
        PullRequestEvent.append(event)
    elif event_type == "IssuesEvent":
        IssuesEvent.append(event)
    elif event_type == "ForkEvent":
        ForkEvent.append(event)
    elif event_type == "GollumEvent":
        GollumEvent.append(event)
    elif event_type == "IssueCommentEvent":
        IssueCommentEvent.append(event)
    elif event_type == "DeleteEvent":
        DeleteEvent.append(event)
    elif event_type == "PullRequestReviewCommentEvent":
        PullRequestReviewCommentEvent.append(event)
    elif event_type == "CommitCommentEvent":
        CommitCommentEvent.append(event)
    elif event_type == "MemberEvent":
        MemberEvent.append(event)
    elif event_type == "PublicEvent":
        PublicEvent.append(event)

    print("¡Evento creado con éxito!")

# Función para mostrar todos los eventos almacenados
def read_events():
    print("Listado de eventos:")
    print("CreateEvent:", CreateEvent)
    print("PushEvent:", PushEvent)
    print("WatchEvent:", WatchEvent)
    print("ReleaseEvent:", ReleaseEvent)
    print("PullRequestEvent:", PullRequestEvent)
    print("IssuesEvent:", IssuesEvent)
    print("ForkEvent:", ForkEvent)
    print("GollumEvent:", GollumEvent)
    print("IssueCommentEvent:", IssueCommentEvent)
    print("DeleteEvent:", DeleteEvent)
    print("PullRequestReviewCommentEvent:", PullRequestReviewCommentEvent)
    print("CommitCommentEvent:", CommitCommentEvent)
    print("MemberEvent:", MemberEvent)
    print("PublicEvent:", PublicEvent)

# Función para actualizar un evento existente
def update_event():
    # Solicitar al usuario los detalles del evento a actualizar
    event_type = input("Ingresa el tipo de evento que deseas actualizar: ")
    event_index = int(input("Ingresa el índice del evento que deseas actualizar: "))
    new_actor_id = input("Ingresa el nuevo ID del actor: ")
    new_actor_login = input("Ingresa el nuevo login del actor: ")
    new_actor_avatar_url = input("Ingresa la nueva URL del avatar del actor: ")
    new_repo_id = input("Ingresa el nuevo ID del repositorio: ")
    new_repo_name = input("Ingresa el nuevo nombre del repositorio: ")
    new_is_public = input("Ingresa si es público (True/False): ")

    # Crear un diccionario con los nuevos detalles del evento
    event = {
        "event_type": event_type,
        "actor": {
            "id": new_actor_id,
            "login": new_actor_login,
            "avatar_url": new_actor_avatar_url
        },
        "repo": {
            "id": new_repo_id,
            "name": new_repo_name
        },
        "public": new_is_public
    }

    # Actualizar el evento en la lista correspondiente según su tipo
    if event_type == "CreateEvent":
        CreateEvent[event_index] = event
    elif event_type == "PushEvent":
        PushEvent[event_index] = event
    elif event_type == "WatchEvent":
        WatchEvent[event_index] = event
    elif event_type == "ReleaseEvent":
        ReleaseEvent[event_index] = event
    elif event_type == "PullRequestEvent":
        PullRequestEvent[event_index] = event
    elif event_type == "IssuesEvent":
        IssuesEvent[event_index] = event
    elif event_type == "ForkEvent":
        ForkEvent[event_index] = event
    elif event_type == "GollumEvent":
        GollumEvent[event_index] = event
    elif event_type == "IssueCommentEvent":
        IssueCommentEvent[event_index] = event
    elif event_type == "DeleteEvent":
        DeleteEvent[event_index] = event
    elif event_type == "PullRequestReviewCommentEvent":
        PullRequestReviewCommentEvent[event_index] = event
    elif event_type == "CommitCommentEvent":
        CommitCommentEvent[event_index] = event
    elif event_type == "MemberEvent":
        MemberEvent[event_index] = event
    elif event_type == "PublicEvent":
        PublicEvent[event_index] = event

    print("¡Evento actualizado con éxito!")

# Función para eliminar un evento existente
def delete_event():
    # Solicitar al usuario el tipo de evento y el índice del evento a eliminar
    event_type = input("Ingresa el tipo de evento que deseas eliminar: ")
    event_index = int(input("Ingresa el índice del evento que deseas eliminar: "))

    # Eliminar el evento de la lista correspondiente según su tipo
    if event_type == "CreateEvent":
        del CreateEvent[event_index]
    elif event_type == "PushEvent":
        del PushEvent[event_index]
    elif event_type == "WatchEvent":
        del WatchEvent[event_index]
    elif event_type == "ReleaseEvent":
        del ReleaseEvent[event_index]
    elif event_type == "PullRequestEvent":
        del PullRequestEvent[event_index]
    elif event_type == "IssuesEvent":
        del IssuesEvent[event_index]
    elif event_type == "ForkEvent":
        del ForkEvent[event_index]
    elif event_type == "GollumEvent":
        del GollumEvent[event_index]
    elif event_type == "IssueCommentEvent":
        del IssueCommentEvent[event_index]
    elif event_type == "DeleteEvent":
        del DeleteEvent[event_index]
    elif event_type == "PullRequestReviewCommentEvent":
        del PullRequestReviewCommentEvent[event_index]
    elif event_type == "CommitCommentEvent":
        del CommitCommentEvent[event_index]
    elif event_type == "MemberEvent":
        del MemberEvent[event_index]
    elif event_type == "PublicEvent":
        del PublicEvent[event_index]

    print("¡Evento eliminado con éxito!")

# Menú principal del programa
while True:
    # Mostrar las opciones disponibles en el menú
    print("\nMenú:")
    print("1. Crear evento")
    print("2. Leer eventos")
    print("3. Actualizar evento")
    print("4. Eliminar evento")
    print("5. Salir")

    # Solicitar al usuario que elija una opción
    choice = input("Seleccione una opción: ")

    # Realizar la acción correspondiente según la opción seleccionada por el usuario
    if choice == "1":
        create_event()
    elif choice == "2":
        read_events()
    elif choice == "3":
        update_event()
    elif choice == "4":
        delete_event()
    elif choice == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

# Guardar los eventos creados en un archivo JSON llamado 'eventos.json'
with open("eventos.json", "w") as outfile:
    json.dump(CreateEvent, outfile)  # Solo se está guardando la lista de eventos de tipo CreateEvent
