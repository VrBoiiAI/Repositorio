from tabulate import *
import csv
import os
import sys

registro = []
columnas = ['Matricula', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Estructura Datos', 'Funciones', 'Databases', 'OOP', 'Valores', 'Redes', 'Promedio']

def cls():
    os.system("cls")

def leer():
    with open('alumni.txt', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            registro.append(line)

def escribir():
    with open('alumni.txt', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(registro)

def menu():
    cls()
    op = input('\n[1] Registrar alumno\n[2] Ver alumnos registrados\n[3] Calificar alumno\n[4] Consultar\n[5] Salir\n\nQue accion desea realizar?\n')

    if op == '1':
        cls()
        agg()
    elif op == '2':
        cls()
        verCon()
    elif op == '3':
        cls()
        calificar()
        escribir()
    elif op == '4':
        consultar()
    elif op == '5':
        escribir()
        sys.exit()
      
    else:
        input('Opcion no valida\nIntente de nuevo')
        menu()

def agg():
    conf = True
    name = input('Ingrese su nombre: ').title()
    apellidoP = input('Ingrese su apellido paterno: ').title()
    apellidoM = input('Ingrese su apellido materno: ').title()
    mat = input('Ingrese su matricula: ').upper()
    for i in registro:
        if mat == i[0]:
            input('La matricula ya está registrada. ')
            menu()
            conf = False
            break
            
    if conf == True:
        registro.append([mat, name, apellidoP, apellidoM])
        for i in range(7):
            registro[-1].append('N/R')
        escribir()
        input("Alumno registrado correctamente. ")
        menu()

def verCon():
    print(tabulate(registro, headers=columnas, tablefmt="fancy_grid"))
    input('Enter para continuar...')
    menu()
    
def calificar():
    conf = False
    mat = input('Ingrese la matricula a calificar: ').upper()
    for i in registro:
        if mat == i[0]:
            index = registro.index(i)
            conf = True
            break

    if conf == True:
        ds = float(input('Ingrese su calificacion de estructura de datos: '))
        (registro[index])[4] = ds
        funciones = float(input('Ingrese su calificacion de funciones: '))
        (registro[index])[5] = funciones
        db = float(input('Ingrese su calificacion de bases de datos: '))
        (registro[index])[6] = db
        oop = float(input('Ingrese su calificacion de programacion: '))
        (registro[index])[7] = oop
        valores = float(input('Ingrese su calificacion de valores: '))
        (registro[index])[8] = valores
        redes = float(input('Ingrese su calificacion de redes: '))
        (registro[index])[9] = redes
        prom = (ds + funciones + db + oop + valores + redes) / 6
        (registro[index])[10] = round(prom, 1)

    else:
        input('Matricula no encontrada. Intente de nuevo.')

    menu()

def consultar():
    cls()
    op = input('Buscar por...\n[1] Matricula\n[2] Nombre\n[3] Apellido\n\n')
    if op == '1':
        buscar = []
        mat = input('Ingrese la matricula a buscar: ').upper()
        for i in registro:
            if mat == i[0]:
                buscar.append(i)
        if buscar != []:
            print(tabulate(buscar, headers=columnas, tablefmt="fancy_grid"))
            input('Enter para continuar...')
            menu() 
        else:
            input("Su busqueda no devolvió resultados, intente con otra consulta.")
            consultar()
        
    elif op == '2':
        buscar = []
        name = input('Ingrese el nombre a buscar: ').capitalize()
        for i in registro:
            if name == i[1]:
                buscar.append(i)
        if buscar != []:
            print(tabulate(buscar, headers=columnas, tablefmt="fancy_grid"))
            input('Enter para continuar...')
            menu()
        else:
            input("Su busqueda no devolvió resultados, intente con otra consulta.")
            consultar()

    elif op == '3':
        buscar = []
        apellido = input('Ingrese el apellido a buscar: ').capitalize()
        for i in registro:
            if apellido == i[2] or apellido == i[3]:
                buscar.append(i)
        if buscar != []:
            print(tabulate(buscar, headers=columnas, tablefmt="fancy_grid"))
            input('Enter para continuar...')
            menu()
        else:
            input("Su busqueda no devolvió resultados, intente con otra consulta.")
            consultar()

    else:
        input("Opcion no válida, intente de nuevo.")
        consultar()

leer()
menu()