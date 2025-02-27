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
        return diccionario
    else:
        print(f"El archivo {nombre_archivo} no existe.")
        return {}

# Función para mostrar el contenido del diccionario y navegar por él
def ver_diccionario(diccionario):
    if diccionario:
        print("\nContenido del diccionario:")
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")
        
        # Preguntar si quiere ver el detalle de una clave
        clave = input("\nIntroduce la clave que deseas ver (o presiona Enter para volver al menú): ")
        
        if clave:
            if clave in diccionario:
                print(f"{clave}: {diccionario[clave]}")
            else:
                print("La clave no existe en el diccionario.")
    else:
        print("El diccionario está vacío o no ha sido cargado.")

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Crear un nuevo diccionario")
    print("2. Cargar un diccionario desde un archivo")
    print("3. Guardar el diccionario actual")
    print("4. Ver contenido del diccionario")
    print("5. Salir")

# Función principal
def main():
    diccionario = {}
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Crear un nuevo diccionario
            diccionario = {}
            print("Nuevo diccionario creado.")
        elif opcion == '2':
            # Cargar un diccionario desde un archivo
            nombre_archivo = input("Introduce el nombre del archivo a cargar: ")
            diccionario = cargar_diccionario(nombre_archivo)
        elif opcion == '3':
            # Guardar el diccionario actual en un archivo
            nombre_archivo = input("Introduce el nombre del archivo para guardar: ")
            guardar_diccionario(diccionario, nombre_archivo)
        elif opcion == '4':
            # Ver el contenido del diccionario
            ver_diccionario(diccionario)
        elif opcion == '5':
            # Salir
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción del menú.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
