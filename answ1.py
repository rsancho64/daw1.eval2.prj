import json
import os

# Función para guardar el diccionario en un archivo
def guardar_diccionario(diccionario, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(diccionario, archivo, indent=4)
    print(f"Diccionario guardado en {nombre_archivo}")

# Función para cargar un diccionario desde un archivo
def cargar_diccionario(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            diccionario = json.load(archivo)
        print(f"Diccionario cargado desde {nombre_archivo}")
        print(f"Nombre del diccionario: {diccionario.get('nombre', 'Desconocido')}")
        print("Contenido del diccionario:")
        for clave, valor in diccionario.items():
            if clave != 'nombre':  # Excluimos la clave 'nombre' para evitar mostrarla como un dato del diccionario.
                print(f"{clave}: {valor}")
        return diccionario
    else:
        print(f"El archivo {nombre_archivo} no existe.")
        return {}

# Función para crear un nuevo diccionario y asignarle un nombre
def crear_diccionario():
    nombre = input("Introduce el nombre del diccionario: ")
    diccionario = {'nombre': nombre}  # Guardamos el nombre del diccionario como una clave especial
    print(f"Diccionario '{nombre}' creado.")
    return diccionario

# Función para agregar un nuevo dato al diccionario
def agregar_dato(diccionario):
    clave = input("Introduce la clave para el nuevo dato: ")
    valor = input(f"Introduce el valor para '{clave}': ")
    diccionario[clave] = valor
    print(f"Se ha agregado la clave '{clave}' con el valor '{valor}'.")

# Función para editar un dato existente en el diccionario
def editar_dato(diccionario):
    clave = input("Introduce la clave del dato que deseas editar: ")
    if clave in diccionario:
        nuevo_valor = input(f"Introduce el nuevo valor para '{clave}': ")
        diccionario[clave] = nuevo_valor
        print(f"El valor de la clave '{clave}' ha sido actualizado a '{nuevo_valor}'.")
    else:
        print(f"La clave '{clave}' no existe en el diccionario.")

# Función para ver el contenido del diccionario actual
def ver_diccionario(diccionario):
    if diccionario:
        print("\nContenido del diccionario actual:")
        for clave, valor in diccionario.items():
            if clave != 'nombre':  # Excluimos la clave 'nombre' que es solo para identificación
                print(f"{clave}: {valor}")
    else:
        print("No hay datos en el diccionario.")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Crear un nuevo diccionario")
    print("2. Cargar un diccionario desde un archivo")
    print("3. Agregar un nuevo dato al diccionario")
    print("4. Editar un dato existente del diccionario")
    print("5. Ver diccionario actual")
    print("6. Guardar el diccionario actual")
    print("7. Salir")

# Función principal
def main():
    diccionario = {}
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Crear un nuevo diccionario
            diccionario = crear_diccionario()
        elif opcion == '2':
            # Cargar un diccionario desde un archivo
            nombre_archivo = input("Introduce el nombre del archivo a cargar: ")
            diccionario = cargar_diccionario(nombre_archivo)
        elif opcion == '3':
            # Agregar un nuevo dato al diccionario
            if diccionario:
                agregar_dato(diccionario)
            else:
                print("Primero debes crear o cargar un diccionario.")
        elif opcion == '4':
            # Editar un dato existente del diccionario
            if diccionario:
                editar_dato(diccionario)
            else:
                print("Primero debes crear o cargar un diccionario.")
        elif opcion == '5':
            # Ver el diccionario actual
            if diccionario:
                ver_diccionario(diccionario)
            else:
                print("No hay diccionario cargado o creado.")
        elif opcion == '6':
            # Guardar el diccionario actual en un archivo
            if diccionario:
                nombre_archivo = input("Introduce el nombre del archivo para guardar: ")
                guardar_diccionario(diccionario, nombre_archivo)
            else:
                print("No hay diccionario para guardar.")
        elif opcion == '7':
            # Salir
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción del menú.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
