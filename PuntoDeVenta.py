import os
import time
import csv

inventario = []  #[[Descripcion, Precio, Codigo, Cantidad],..]
ventaTotal = [0]  #[Total suma, codigos de producto...]
ticket = [
  " " + "-" * 75 +
  "\n|             Descripcion             | precio |   codigo   | cant. | total |"
  + "\n " + "-" * 75
]
lista = ''


def setup(
):  #Se ejecuta al iniciar el programa, escribe 'productos.txt' en la lista inventario y crea la lista (menu)
  with open('productos.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
      inventario.append(line)

  for i in inventario:
    i[1] = float(i[1])
    i[3] = int(i[3])
    i[-1] = int(i[-1])

  global lista
  for i in inventario:
    lista += f'- {i[0]} - ${i[1]} - {i[2]}\n'


def escribir():
  with open('productos.txt', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(inventario)


def printicket():
  if ticket != [
      " " + "-" * 75 +
      "\n|             Descripcion             | precio |   codigo   | cant. | total |"
      + "\n " + "-" * 75
  ]:
    for i in ticket:
      print(i)
    print('\n')


def verify(pregunta, tipo, rango=[]):
  while True:
    var = input(pregunta)
    try:
      var = tipo(var)
    except:
      print('Dato no valido. Intente de nuevo')
    if type(var) == tipo:
      if rango == []:
        break
      elif var >= rango[0] and var <= rango[1]:
        break
      else:
        print('Valor fuera de las opciones.')

  return var


def menu():
  global ventaTotal, ticket
  os.system('cls')
  op = input(
    '\n[1] Finalizar Venta\n[2] Continuar Venta\n[3] Cancelar Venta\n\nQue accion desea realizar?\n'
  )
  if op == '1':
    for i in inventario:
      if i[2] in ventaTotal:
        i[-1] = 0
    printicket()
    print(f'Total {"."*(66-len(str(ventaTotal[0])))}  ${ventaTotal[0]}')
    ventaTotal = [0]
    ticket = [
      " " + "-" * 75 +
      "\n|             Descripcion             | precio |   codigo   | cant. | total |"
      + "\n " + "-" * 75
    ]
    input('Enter para realizar otra venta...')
    escribir()
    venta()
  elif op == '2':
    venta()
  elif op == '3':
    os.system('cls')
    op = input(
      '\n[1] Cancelar Venta\n[2] Eliminar Producto\n\nQue accion desea realizar?\n'
    )
    if op == '1':
      for i in inventario:
        if i[2] in ventaTotal:
          i[-1] = 0

      ventaTotal = [0]
      ticket = [
        " " + "-" * 75 +
        "\n|             Descripcion             | precio |   codigo   | cant. | total |"
        + "\n " + "-" * 75
      ]
      input('Enter para realizar otra venta...')
      venta()

    elif op == '2':
      printicket()
      code = input(
        'Ingrese el codigo del producto que desea eliminar: ').upper()
      if code in ventaTotal:
        ventaTotal.remove(code)
        for i in inventario:
          if i[2] == code:
            i[-1] = 0
            ventaTotal[0] -= i[1] * i[-2]
        for i in ticket:
          if code in i:
            index = ticket.index(i)
            ticket.pop(index)
            ticket.pop(index)

      else:
        print('El producto no está en la lista...')
        menu()
      venta()

  else:
    pass


def venta():
  os.system('cls')
  printicket()
  print(lista)
  code = input(
    "\nIngrese el codigo del producto ('M' para ir al menú): ").upper()
  conf = False
  for i in inventario:
    if code == i[2]:
      #print('\n')
      if not (i[-2] <= 0):
        i[-1] += 1
        i[-2] -= 1
        if i[2] not in ventaTotal:
          ticket.append(
            f'| {i[0]}{" "*(36-len(i[0]))}| {i[1]}{" "*(7-len(str(i[1])))}| {i[2]}{" "*(11-len(i[2]))}| {i[-1]}{" "*(6-len(str(i[-1])))}| {i[1]*i[4]}{" "*(6-len(str(i[1]*i[4])))}|'
          )
          ticket.append(" " + "-" * 75)
          ventaTotal.append(i[2])
          ventaTotal[0] += i[1]
          conf = True

        else:
          for j in ticket:
            if i[0] in j:
              ventaTotal[0] += i[1]
              ind = ticket.index(j)
              ticket.pop(ind)
              ticket.pop(ind)
              ticket.append(
                f'| {i[0]}{" "*(36-len(i[0]))}| {i[1]}{" "*(7-len(str(i[1])))}| {i[2]}{" "*(11-len(i[2]))}| {i[-1]}{" "*(6-len(str(i[-1])))}| {i[1]*i[4]}{" "*(6-len(str(i[1]*i[4])))}|'
              )
              ticket.append(" " + "-" * 75)
              conf = True

        venta()

      else:
        os.system("cls")
        print("No hay mas existencia de este producto :(")
        time.sleep(2)
        venta()

  if code == 'm' or code == 'M':
    conf = True
    menu()

  if conf == False:
    for i in range(2):
      os.system("cls")
      print("No existe el producto.")
      time.sleep(.4)
      os.system("cls")
      print("No existe el producto..")
      time.sleep(.4)
      os.system("cls")
      print("No existe el producto...")
      time.sleep(.4)
    venta()


setup()
venta()
