import json
import os

d = {}

# ---------------------------------------------------
def _save(fname):
    with open(fname, 'w') as archivo:
        json.dump(d, archivo, indent=4)
    print(f"d guardado en {fname}")

# ---------------------------------------------------
def _load(fname):
    if os.path.exists(fname):
        with open(fname, 'r') as f: d = json.load(f)
        print(f"d loaded from {fname}")
        print(f"d name: {d.get('nombre', 'Desconocido')}")
        print(f"d contents:")
        for clave, valor in d.items():
            # Excluimos la clave 'nombre' para evitar mostrarla como un dato del d.
            if clave != 'nombre':
                print(f"{clave}: {valor}")
        return d
    else:
        print(f"El archivo {fname} no existe.")
        return {}

# ---------------------------------------------------
def _new():
    nombre = input("Introduce el nombre del d: ")
    d = {'nombre': nombre}  # el nombre del d como clave especial
    print(f"d '{nombre}' creado.")
    return d

# ---------------------------------------------------
def _addPairKV(d):
    clave = input("Introduce la clave para el nuevo dato: ")
    valor = input(f"Introduce el valor para '{clave}': ")
    d[clave] = valor
    print(f"Se ha agregado la clave '{clave}' con el valor '{valor}'.")

# ---------------------------------------------------
def _updatePairKV(d):
    clave = input("Introduce la clave del dato que deseas editar: ")
    if clave in d:
        nuevo_valor = input(f"Introduce el nuevo valor para '{clave}': ")
        d[clave] = nuevo_valor
        print(f"El valor de la clave '{
              clave}' ha sido actualizado a '{nuevo_valor}'.")
    else:
        print(f"La clave '{clave}' no existe en el d.")

# ---------------------------------------------------
def _print(d):
    if d:
        print("\nContenido del d actual:")
        for clave, valor in d.items():
            if clave != 'nombre':  # Excluimos la clave 'nombre' que es solo para identificación
                print(f"{clave}: {valor}")
    else:
        print("No hay datos en el d.")

# ---------------------------------------------------
def mostrar_menu2():
    print("help")    
    print("new")
    print("print")
    print("exit")
    print("load  <fileName>")
    print("saveTo <fileName>")
    print("eval <k>")    / -> v    
    print("add <k> <w>") / new k
    print("set <k> <w>") / updatable k

# ---------------------------------------------------
def main():

    while True:

        cmd = input("?? : ")
        tok = cmd.split()
        print("parsed: ", tok)

        if len(tok) == 1:

            if tok[0] == 'help':
                mostrar_menu2()
                break
            if tok[0] == 'new':
                d = _new()
                break
            if tok[0] == 'print':
                _print(d)
                break
            if tok[0] == 'exit':
                print("BYE")
                break

        if len(tok) == 2:

            fname = arg = tok[1]

            if tok[0] == 'load':
                d = _load(fname)
                break

            if tok[0] == 'saveTo':
                _save(fname)
                break

            fname = arg = tok[1]


        if tok[0] == 'load':

        if !d:
            print("No d cargado/creado.")
            break
        if tok[0] == 'add':
            _addPairKV(d, k, v)
            break
        if tok[0] == '4':
            _updatePairKV(d)
            break

        elif tok[0] == '6':
            if d:
                fname = input("archivo a guardar: ")

            else:
                print("No d cargado/creado.")
        else:
            print("Opción no válida. Por favor selecciona una opción del menú.")


if __name__ == "__main__":
    main()
