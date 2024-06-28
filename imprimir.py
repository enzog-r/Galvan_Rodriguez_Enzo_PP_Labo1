def imprimir_lista(lista: list):
    """
    La funcion imprimir_lista muestra por pantalla la lista de datos en columnas.
    parametro: lista: Es la lista de datos que vamos a mostrar por pantalla
    """
    if not lista:
        print("La lista esta vacia.")
        return

    claves = list(lista[0].keys())

    anchos = [len(clave) for clave in claves]
    for elemento in lista:
        for i, clave in enumerate(claves):
            anchos[i] = max(anchos[i], len(str(elemento[clave])))

    for i, clave in enumerate(claves):
        print(clave + " " * (anchos[i] - len(clave)), end=" ")
    print()

    for ancho in anchos:
        print("-" * ancho, end=" ")
    print()

    for elemento in lista:
        for i, clave in enumerate(claves):
            valor = str(elemento[clave])
            print(valor + " " * (anchos[i] - len(valor)), end=" ")
        print()
