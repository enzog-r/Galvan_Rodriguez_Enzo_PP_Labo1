import json


def cargar_archivo(nombre: str) -> list:
    """
    La funcion cargar_archivo lee un archivo tipo JSON y lo vuelve una lista

    parametro: nombre recibe un tipo string del nombre del archivo
    return lista retorna la lista de datos creada en caso contrario retorna falso
    """
    try:
        with open(nombre, "r") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return False
