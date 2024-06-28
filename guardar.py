import json


def guardar_json(datos: list, nombre_archivo: str):
    """
    La funcion guardar_json crea un archivo .json a partir de una lista de datos.
    parametros: datos: Es la lista de datos.
                nombres_archivos: El nombre que le pondremos al archivo.
    return: True si lo crea, False si no lo crea.
    """
    if not datos:
        print("La lista esta vacia.")
        return

    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)

        print(f"Se creó el archivo: {nombre_archivo}")
        return True

    except IOError:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False
