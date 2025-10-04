import os
import csv
import sys

agenda = []

def setup():  #Se ejecuta al iniciar el programa, escribe 'agenda.txt' en la lista agenda
  with open('agenda.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
      agenda.append(line)
      
def escribir():
  with open('agenda.txt', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(agenda)

def menu():
	op = input('[1] Agregar contacto\n[2] Ver contactos guardados\n[3] Eliminar contacto\n[4] Salir\n\nQue accion desea realizar?\n')
	if op == '1':
		os.system('cls')
		agg()

	elif op == '2':
		os.system('cls')
		verCon()

	elif op == '3':
		os.system('cls')
		borrar()
  
	elif op == '4':
		sys.exit()

	else:
		os.system('cls')
		print('Opcion no valida\nIntente de nuevo\n')
		menu()

def agg():
	name = input('Ingrese su nombre: ').title()
	last_name = input('Ingrese su apellido: ').title()
	tel = input('Ingrese su numero de telefono: ').title()
	agenda.append([name, last_name, tel])
	escribir()
	os.system('cls')
	menu()

def verCon():
	if agenda != []:
		for i in agenda:
			j = agenda.index(i)
			print(f'[{j+1}] {i[0]}\n')

		op = input('\nSeleccione un contacto para ver\nEnter para salir al menu...\n')
		if op == '':
			os.system('cls')
			menu()

		else:
			try:
				op = int(op)-1

			except:
				os.system('cls')
				print('Ingrese un numero de contacto válido\n')
				verCon()

			try:
				print(f'\n{(agenda[op][0])} {(agenda[op][1])} {(agenda[op][2])}\n')
				input('Enter para continuar...')
				os.system('cls')
				menu()

			except:
				os.system('cls')
				print('Ingrese un numero de contacto disponible\n')
				verCon()
	else:
		print("Agenda vacía. Agrega a un contacto!\n")
		menu()
		

def borrar():
	for i in agenda:
		j = agenda.index(i)
		print(f'[{j+1}] {i[0]}\n')

	op = input('\nSeleccione un contacto para eliminar\nEnter para cancelar...\n')
	if op == '':
		os.system('cls')
		menu()

	else:
		try:
			op = int(op)-1

		except:
			os.system('cls')
			print('Ingrese un numero de contacto válido\n')
			borrar()

		try:
			os.system('cls')
			print(f'\n{(agenda[op][0])} {(agenda[op][1])} {(agenda[op][2])}\n')
			agenda.pop(op)
			input('Contacto eliminado\nEnter para continuar...')
			escribir()
			os.system('cls')
			menu()

		except:
			os.system('cls')
			print('Ingrese un numero de contacto disponible\n')
			verCon()
	

os.system('cls')
setup()
menu()
