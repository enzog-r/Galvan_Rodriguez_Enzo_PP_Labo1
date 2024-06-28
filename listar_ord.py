from imprimir import imprimir_lista


def listar_por_clave(lista: list, clave: str, reverse=False):
    """
    La funcion listar_por_clave muestra por pantalla la lista de datos ordenada.
    parametros: lista: Es la lista de datos.
                clave: El valor por el cual ordenaremos la lista.
                reverse: Es un valor booleano por si queremos poner la lista de forma descendente.
    return: lista: Es la lista de datos ordenada.
    """
    if not lista or clave not in lista[0]:
        print("Clave no encontrada.")

    lista.sort(key=lambda elemento: elemento[clave], reverse=reverse)
    imprimir_lista(lista)
    return lista
