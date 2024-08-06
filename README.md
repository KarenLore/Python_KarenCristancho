# Python
Este proyecto contiene una serie de scripts de Python organizados por días. Cada día incluye uno o más archivos .py que contienen el código correspondiente a ese día. Los scripts abordan diferentes temas y desafíos relacionados con Python.

## Tabla de contenidos
| Indice | Titulo  |
|--|--|
| 1 | Día1 Main |
| 2 | Día2 Fibonacci, intentos, secreto |
| 3 | Día3 Funciones |
| 4 | Día4 Money_Change |
| 5 | Día5 Ejercicio 1 y 2 |
| 6 | Día6 Ejercicio 1 y 2 |
| 7 | Día7 Trabajo_grupal |
| 8 | Día8 Ejercicio 1 y 2 |
| 9 | Día9 Carrito |
| 10 | Día10 Ejercicio 1 |
| 11 | Día11 Ejercicio1, Eventos y Large-File |
| 12 | Día12 Ejercicio2, Eventos y Large-File |
| 13 | Día13 Info y Main |

### Instalación
Deberas ejecutar el comando git clone para copiar el repositorio
  [Link](https://github.com/KarenLore/Python_KarenCristancho.git)

``` bash
sudo apt install app
```

``` Código realizado en:
- Python
- Json
```
## Sección 1 
### Día1 Main
### Descripción
En este día, se introducen los conceptos básicos de Python, comenzando con la impresión de "Hola Mundo" y explorando varios tipos de datos primitivos como números, decimales, booleanos y cadenas de texto. Se muestra cómo ingresar información a través del teclado utilizando input() y cómo convertir tipos de variables entre sí. Además, se explican los bucles for y while para iterar sobre secuencias de números. El día concluye con una introducción a las funciones, incluyendo ejemplos de funciones sin parámetros, con parámetros, con valores de retorno y combinaciones de estos

## Sección 2 
### Día2 Fibonacci, intentos, secreto
### Descripción
En este día, se presentan tres programas interactivos escritos en Python:
- Secuencia de Fibonacci:
Este programa genera la secuencia de Fibonacci hasta el número ingresado por el usuario. Explica la lógica detrás de la secuencia y permite al usuario decidir si quiere continuar o salir. Utiliza bucles y condicionales para generar e imprimir la secuencia.
- Juego de Adivinanza del Número Secreto (con límite de intentos):
El usuario intenta adivinar un número secreto generado aleatoriamente entre 1 y 100. El programa proporciona pistas sobre si el número secreto es mayor o menor que la suposición del usuario. El usuario tiene un total de 10 intentos para adivinar el número. Si no lo adivina en esos intentos, el juego muestra el número secreto.
- Juego de Adivinanza del Número Secreto (sin límite de intentos):
Similar al programa anterior, este juego también genera un número secreto entre 1 y 100. Sin embargo, en esta versión, el usuario tiene intentos ilimitados para adivinar el número. El programa sigue proporcionando pistas sobre si el número secreto es mayor o menor que la suposición del usuario hasta que se adivine correctamente.

## Sección 3 
### Día3 Funciones
### Descripción
Este programa interactivo ofrece dos funcionalidades principales:
- Verificación de Números Primos: Permite al usuario ingresar un número y determina si es primo, es decir, si solo es divisible por 1 y por sí mismo.
- Generador de Contraseñas Seguras: Permite al usuario crear una contraseña segura de longitud variable, con una combinación de letras, números y caracteres especiales.
El programa incluye un menú sencillo que guía al usuario para seleccionar entre estas opciones o salir.

## Sección 4 
### Día4 Money_Change
### Descripción
Este programa calcula el mínimo número de monedas necesarias para dar un cambio específico utilizando monedas de 1, 5 y 10 unidades.
**Funciones:**
- minimo_numero_monedas(cambio): Dada una cantidad de cambio, calcula el número mínimo de monedas de 1, 5 y 10 unidades necesarias.
**Detalles del Funcionamiento:**
- Monedas de 10: Se calcula la cantidad de monedas de 10 necesarias y se actualiza el valor del cambio restante.
- Monedas de 5: Se calcula la cantidad de monedas de 5 necesarias con el valor restante del cambio.
- Monedas de 1: Se calcula la cantidad de monedas de 1 necesarias para completar el cambio restante.
El programa solicita al usuario que ingrese un valor para el cambio y muestra el número de monedas de cada denominación necesarias, así como el total de monedas.

## Sección 5 
### Día5 Ejercicio 1 y 2
### Descripción
**Contar Pares Divisibles por k**
Dado un número de casos de prueba, para cada caso se leen dos valores: el tamaño de una lista y un número k. Luego, se verifica cuántos pares de elementos en la lista cumplen con la condición de que la suma de los dos elementos sea divisible por k.
-Función Principal: resolver()
**-Entradas:**
- T: Número de casos de prueba.
- Para cada caso: n (número de elementos en la lista), k (número para la operación módulo), y una lista de n enteros.
- Salidas: Para cada caso, imprime el número de pares que cumplen la condición, precedido por "Case x:".
  
**Ajustar Espesores de Monedas a Mesas**
Dado un conjunto de monedas con espesores específicos y alturas de mesas, el programa encuentra la longitud más cercana superior e inferior para cada altura de mesa, basada en los múltiplos de los espesores de las monedas.
**-Entradas:**
- n y t: Número de tipos de monedas y número de mesas.
- Una lista de n enteros que representan los espesores de las monedas.
- Una lista de t enteros que representan las alturas de las mesas.
- Salidas: Para cada altura de mesa, imprime la longitud más cercana superior e inferior en relación con los espesores de las monedas.

**Detalles Técnicos:**
- Map: Convierte las entradas en una lista de enteros.
- Split: Divide las cadenas de texto en partes más pequeñas.
- %: Operador de módulo que devuelve el residuo de una división.
- Max y Min: Encuentra el valor máximo o mínimo en una lista.
  
## Sección 6 
### Día6 Ejercicio 1 y 2
### Descripción
**Eliminar Duplicados y Ordenar Números**
Lee una línea de números separados por espacios, toma hasta los primeros 300 números, elimina los duplicados y los ordena.
- Entradas: Una línea de números separados por espacios.
- Salidas: Lista de números únicos y ordenados.
  
**Encontrar Índices de Números que Suman un Objetivo**
Dada una lista de números y un objetivo, encuentra dos números en la lista que sumen el objetivo y devuelve sus índices.
**Entradas:**
- Lista de números.
- Número entero que es el objetivo.
- Salidas: Índices de los dos números cuya suma es igual al objetivo.

## Sección 7 
### Día7 Trabajo_grupal
### Descripción
Este programa simula una tienda virtual que permite a los usuarios gestionar un carrito de compras. Incluye un catálogo de productos con identificadores únicos, precios y cantidades disponibles. El usuario puede visualizar el catálogo, agregar productos al carrito especificando el ID y la cantidad deseada, y ver el contenido del carrito con detalles de cada producto, cantidad y subtotal. Además, el programa calcula el total de la compra sumando los subtotales de todos los productos en el carrito. El menú principal ofrece opciones para agregar productos, ver el carrito, calcular el total, finalizar la compra o salir del programa.

## Sección 8 
### Día8 Ejercicio 1 y 2
### Descripción
**Este programa incluye dos secciones principales: la gestión de suscripciones para usuarios y el procesamiento de datos de frutas.**
En la primera parte, se define una clase Usuario que permite manejar suscripciones a un servicio. Un usuario puede recargar su saldo, suscribirse a un año específico, mostrar sus suscripciones actuales, y también puede comprar una suscripción como regalo para otro usuario. El menú principal permite a los usuarios interactuar con estas funciones.
En la segunda parte, se realiza el procesamiento de una lista de frutas. Se realizan las siguientes operaciones:
- Se convierten los nombres de las frutas a mayúsculas.
- Se filtran las frutas cuyo precio es inferior a 0.50.
- Se encuentra la fruta con la mayor cantidad disponible.
- Se ordenan las frutas en función del valor en stock (cantidad multiplicada por precio), de mayor a menor.
Cada operación se realiza utilizando técnicas de manipulación de listas y funciones lambda para realizar cálculos y filtrados específicos.

## Sección 9 
### Día9 Carrito
### Descripción
Este código permite al usuario agregar productos a un carrito de compras. Primero, el usuario ingresa la cantidad de productos que desea agregar. Luego, en un bucle, solicita el nombre, el precio y la cantidad de cada producto, y los agrega al carrito como tuplas en una lista. Después de agregar todos los productos, se imprime la lista de productos en el carrito, mostrando el nombre, el precio y la cantidad de cada uno.

## Sección 10 
### Día10 Ejercicio 1
### Descripción
Este código define una función posicion que busca en una lista de números el primer índice donde el valor es mayor o igual a un objetivo dado. Si encuentra tal valor, devuelve su índice. Si no, devuelve la longitud de la lista. El usuario ingresa los números separados por comas y el objetivo, y el programa imprime la posición del objetivo en la lista.

## Sección 11 
### Día11 Ejercicio1, Eventos y Large-File
### Descripción
Este código maneja eventos almacenados en un archivo JSON. Primero, abre y carga el archivo large-file.json en una lista. Luego, presenta un menú para revisar, crear, actualizar y eliminar eventos.
- Revisar Evento: Muestra todos los eventos con su ID, tipo, actor, repositorio, login y URL de avatar.
- Crear Evento: Permite al usuario agregar nuevos eventos a la lista.
- Actualizar Evento: Permite al usuario modificar el tipo e ID de un evento existente.
- Eliminar Evento: Permite al usuario eliminar un evento de la lista.
Finalmente, guarda los cambios en un archivo JSON llamado eventos.json.

## Sección 12 
### Día11 Ejercicio2, Eventos y Large-File
### Descripción
Este código gestiona diferentes tipos de eventos (como CreateEvent, PushEvent, etc.) utilizando listas separadas para cada tipo.
- Cargar Datos: Lee los datos desde un archivo JSON (large-file.json) y los almacena en listas vacías según el tipo de evento.
- Crear Evento: Permite al usuario ingresar detalles para un nuevo evento y lo agrega a la lista correspondiente.
- Leer Eventos: Muestra todos los eventos almacenados en cada lista.
- Actualizar Evento: Permite al usuario modificar un evento existente en la lista según su tipo.
- Eliminar Evento: Permite al usuario eliminar un evento específico de la lista.
El programa tiene un menú para seleccionar estas opciones y guarda los eventos en un archivo JSON (eventos.json) al finalizar, pero actualmente solo guarda la lista de eventos de tipo CreateEvent.

## Sección 13 
### Día13 Info y Main
### Descripción
Este código maneja una base de datos de estudiantes mediante un archivo JSON llamado info.json. Ofrece una serie de funciones para interactuar con esta base de datos y realizar operaciones básicas sobre la información de los estudiantes:
- Abrir Archivo: La función abrirArchivo() carga los datos desde el archivo JSON en una estructura de datos de Python, permitiendo su manipulación.
- Guardar Archivo: La función guardarArchivo(miData) escribe los datos actuales en el archivo JSON, actualizando la información almacenada con los cambios realizados.
- Mostrar Estudiantes: mostrarEstudiantes(estudiantes) recorre la lista de estudiantes y muestra los detalles de cada uno, incluyendo ID, nombre, apellido, edad, fecha de nacimiento, cédula, email y GitHub.
- Modificar Estudiante: modificarEstudiante(estudiantes) permite al usuario seleccionar un estudiante por su ID y actualizar uno de sus campos. Los campos que se pueden modificar incluyen nombre, apellido, edad, fecha de nacimiento, cédula, email y GitHub. Una vez realizado el cambio, se guarda la información actualizada en el archivo JSON.
- Crear Estudiante: crearEstudiante(estudiantes) solicita al usuario la información completa para un nuevo estudiante, asigna un ID único y añade el nuevo estudiante a la lista. Luego, guarda la lista actualizada en el archivo JSON.
- Eliminar Estudiante: eliminarEstudiante(estudiantes) permite al usuario seleccionar un estudiante por su ID para eliminarlo de la lista. Después de eliminar el estudiante, se actualiza el archivo JSON con la lista de estudiantes modificada.
El menú principal del programa ofrece opciones para revisar la lista de estudiantes, modificar un registro existente, crear un nuevo estudiante, eliminar un estudiante o finalizar el programa. Dependiendo de la opción seleccionada, se ejecuta la función correspondiente y se actualiza el archivo JSON con los cambios realizados.

Hecho por ***Karen Lorena Cristancho Caceres***

> Notas Importantes
> [!NOTE]
> Cada script está diseñado para ser ejecutado individualmente y abarca diferentes conceptos de Python, proporcionando una manera práctica de aprender y aplicar conocimientos.

> [!TIP]
> Asegúrate de entender el código de cada día antes de pasar al siguiente. Esto te ayudará a construir una base sólida en Python

> [!IMPORTANT]
> Algunos scripts pueden requerir bibliotecas adicionales. Consulta el código y asegúrate de tener todas las dependencias instaladas antes de ejecutar los scripts.

> [!WARNING]
> Los scripts deben ser probados en un entorno controlado para evitar cualquier problema de rendimiento o compatibilidad.

> [!CAUTION]
> No modifiques los scripts sin comprender completamente su funcionamiento. Esto podría llevar a errores inesperados.

### 📞Contacto
  Para preguntas, sugerencias o más información sobre el proyecto, no dudes en ponerte en contacto conmigo:
   - Nombre: Karen Lorena Cristancho
   - Email: karenlorenacriscaceres@gmail.com
