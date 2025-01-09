import json
import os

# ---------------------------------------------------
def guardar_d(d, fname):
    with open(fname, 'w') as archivo:
        json.dump(d, archivo, indent=4)
    print(f"d guardado en {fname}")

# ---------------------------------------------------
def cargar_d(fname):
    if os.path.exists(fname):
        with open(fname, 'r') as archivo:
            d = json.load(archivo)
        print(f"d cargado desde {fname}")
        print(f"Nombre del d: {d.get('nombre', 'Desconocido')}")
        print("Contenido del d:")
        for clave, valor in d.items():
            if clave != 'nombre':  # Excluimos la clave 'nombre' para evitar mostrarla como un dato del d.
                print(f"{clave}: {valor}")
        return d
    else:
        print(f"El archivo {fname} no existe.")
        return {}

# ---------------------------------------------------
def crear_d():
    nombre = input("Introduce el nombre del d: ")
    d = {'nombre': nombre}  # Guardamos el nombre del d como una clave especial
    print(f"d '{nombre}' creado.")
    return d

# ---------------------------------------------------
def agregar_dato(d):
    clave = input("Introduce la clave para el nuevo dato: ")
    valor = input(f"Introduce el valor para '{clave}': ")
    d[clave] = valor
    print(f"Se ha agregado la clave '{clave}' con el valor '{valor}'.")

# ---------------------------------------------------def editar_dato(d):
    clave = input("Introduce la clave del dato que deseas editar: ")
    if clave in d:
        nuevo_valor = input(f"Introduce el nuevo valor para '{clave}': ")
        d[clave] = nuevo_valor
        print(f"El valor de la clave '{clave}' ha sido actualizado a '{nuevo_valor}'.")
    else:
        print(f"La clave '{clave}' no existe en el d.")

# ---------------------------------------------------
def ver_d(d):
    if d:
        print("\nContenido del d actual:")
        for clave, valor in d.items():
            if clave != 'nombre':  # Excluimos la clave 'nombre' que es solo para identificación
                print(f"{clave}: {valor}")
    else:
        print("No hay datos en el d.")

# ---------------------------------------------------
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Crear un nuevo d")
    print("2. Cargar un d desde un archivo")
    print("3. Agregar un nuevo dato al d")
    print("4. Editar un dato existente del d")
    print("5. Ver d actual")
    print("6. Guardar el d actual")
    print("7. Salir")

# ---------------------------------------------------
def main():
    d = {}
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Crear un nuevo d
            d = crear_d()
        elif opcion == '2':
            # Cargar un d desde un archivo
            fname = input("Introduce el nombre del archivo a cargar: ")
            d = cargar_d(fname)
        elif opcion == '3':
            # Agregar un nuevo dato al d
            if d:
                agregar_dato(d)
            else:
                print("Primero debes crear o cargar un d.")
        elif opcion == '4':
            # Editar un dato existente del d
            if d:
                editar_dato(d)
            else:
                print("Primero debes crear o cargar un d.")
        elif opcion == '5':
            # Ver el d actual
            if d:
                ver_d(d)
            else:
                print("No hay d cargado o creado.")
        elif opcion == '6':
            # Guardar el d actual en un archivo
            if d:
                fname = input("Introduce el nombre del archivo para guardar: ")
                guardar_d(d, fname)
            else:
                print("No hay d para guardar.")
        elif opcion == '7':
            # Salir
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor selecciona una opción del menú.")

if __name__ == "__main__":
    main()
