import os
import time
import csv
from tabulate import *

inventario = []  # [[Descripcion, Precio, Codigo, Cantidad],..]
ventaTotal = [0]  # [Total suma, codigos de producto...]
columnas = ["Descripcion", "Precio", "Codigo", "Cantidad", "Total"]
columnas2 = ["Descripcion", "Precio ($)", "Codigo"]
lista = []
# Coca Cola 2L Retornable,27.0,CCR2L,0,0


def cls():
    os.system("cls")


def setup():  # Se ejecuta al iniciar el programa, escribe 'productos.txt' en la lista inventario y crea la lista (menu)
    global lista
    with open("productos.txt", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            inventario.append(line)

    for i in inventario:
        i[1] = float(i[1])
        i[3] = int(i[3])
        i[-1] = int(i[-1])

    for i in inventario:
        lista.append([i[0], i[1], i[2]])


def printProds():
    global lista
    print(tabulate(lista, headers=columnas2))


def escribir():
    with open("productos.txt", "w", newline="") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(inventario)


def printicket():
    global ventaTotal
    data = []
    if ventaTotal != [0]:
        for i in ventaTotal[1:]:
            for j in inventario:
                if i == j[2]:
                    data.append([j[0], j[1], j[2], j[-1]])

        print(tabulate(data, headers=columnas, tablefmt="rounded_grid"))


def menu():
    global ventaTotal
    cls()
    op = input(
        "\n[1] Finalizar Venta\n[2] Continuar Venta\n[3] Cancelar Venta\n\nQue accion desea realizar?\n"
    )
    if op == "1":
        printicket()
        print(f"Total", "." * 30, "$", ventaTotal[0])
        for i in inventario:
            if i[2] in ventaTotal:
                i[-1] = 0
        ventaTotal = [0]
        input("Enter para realizar otra venta...")
        escribir()
        venta()
    elif op == "2":
        venta()
    elif op == "3":
        cls()
        op = input(
            "\n[1] Cancelar Venta\n[2] Eliminar Producto\n\nQue accion desea realizar?\n"
        )
        if op == "1":
            for i in inventario:
                if i[2] in ventaTotal:
                    i[-2] += i[-1]
                    i[-1] = 0
            ventaTotal = [0]
            input("Enter para realizar otra venta...")
            venta()

        elif op == "2":
            printicket()
            code = input("Ingrese el codigo del producto que desea eliminar: ").upper()
            if code in ventaTotal:
                ventaTotal.remove(code)
                for i in inventario:
                    if i[2] == code:
                        ventaTotal[0] -= i[1] * i[-1]
                        i[-1] = 0
                        i[-2] += i[-1]

            else:
                print("El producto no está en la lista...")
                menu()
            venta()

        else:
            input("Opcion no valida. Intente de nuevo.")
        menu()

    else:
        input("Opcion no valida. Intente de nuevo.")
        menu()


def venta():
    cls()
    printicket()
    printProds()
    code = input("\nIngrese el codigo del producto ('M' para ir al menú): ").upper()
    conf = False
    for i in inventario:
        if code == i[2]:
            if i[-2] > 0:
                i[-1] += 1
                i[-2] -= 1
                if i[2] not in ventaTotal:
                    ventaTotal.append(i[2])
                    ventaTotal[0] += i[1]
                    conf = True

                else:
                    ventaTotal[0] += i[1]
                    conf = True

                venta()

            else:
                os.system("cls")
                print("No hay mas existencia de este producto :(")
                time.sleep(2)
                venta()

    if code == "M":
        conf = True
        menu()

    if conf == False:
        for i in range(2):
            os.system("cls")
            print("No existe el producto.")
            time.sleep(0.4)
            os.system("cls")
            print("No existe el producto..")
            time.sleep(0.4)
            os.system("cls")
            print("No existe el producto...")
            time.sleep(0.4)
        venta()


setup()
venta()
