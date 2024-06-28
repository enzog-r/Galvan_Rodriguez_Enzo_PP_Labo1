def asignar_totales(lista: list):
    """
    La funcion asignar_totales calcula el precio total utilizando diferentes claves.
    parametro: lista: Es la lista de datos.
    """
    if not lista:
        print("La lista esta vacia.")
        return

    for elemento in lista:
        cantidad = int(elemento["cantidad"])
        precio = float(elemento["precioUnitario"])
        elemento["totalServicio"] = (lambda cantidad, precio: cantidad * precio)(
            cantidad, precio
        )
    print("Totales asignados.")
