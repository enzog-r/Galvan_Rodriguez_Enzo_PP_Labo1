from menu import mostrar_menu
from cargar import cargar_archivo
from imprimir import imprimir_lista
from asignar import asignar_totales
from listar_ord import listar_por_clave
from guardar import guardar_json

lista = []
lista_desc_ordenada = []

while True:
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        lista = cargar_archivo("compu.json")
        print("Archivo cargado.")

    elif opcion == "2":
        imprimir_lista(lista)

    elif opcion == "3":
        asignar_totales(lista)

    elif opcion == "5":
        lista_desc_ordenada = listar_por_clave(lista, "descripcion")

    elif opcion == "6":
        guardar_json(lista_desc_ordenada, "compu_ordenada.json")

    elif opcion == "7":
        break
