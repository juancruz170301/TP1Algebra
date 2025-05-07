import getpass


admin = "admin@ventaspasajes777.com"
adminC = "admin"
i = 0
usuario = str(input("Ingrese su usario "))
contraseña = getpass.getpass("Ingrese la contraseña ")
ARG = 0
BRA = 0
CHI = 0

codNovedad1 = "1"
textoNovedad1 = "Vuelo reprogramado"
fechaPublicacionNovedad1 = "01/05/2025"
fechaExpiraciónNovedad1 = "16/05/2025"


codNovedad2 = "2"
textoNovedad2 = "Vuelo con demoras"
fechaPublicacionNovedad2 = "06/05/2025"
fechaExpiraciónNovedad2 = "13/05/2025"


codNovedad3 = "3"
textoNovedad3 = "Vuelo suspendido"
fechaPublicacionNovedad3 = "08/05/2025"
fechaExpiraciónNovedad3 = "10/05/2025"

#Validación de datos
while i < 2 and usuario != admin and contraseña != adminC :
	usuario = str(input("Ingrese su usario "))
	contraseña = getpass.getpass("Ingrese la contraseña ")
	i = i + 1

if i >= 2:
	print("Demasiados intentos fallidos, cerrando el programa")
	exit()

#MENÚ DE OPCIONES
print("------------------")
print("Menú del administrador")
print("------------------")
print("1. Gestión de Aerolíneas")
print("2. Aprobar/Denegar Promociones")
print("3. Gestión de Novedades")
print("4. Reportes")
print("5. Salir")

opcion = input("Elija una opción ")

while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion !="5":
	opcion = input("Ingrese una opción válida: ")


while opcion != "5":
	if opcion == "1":#ENTRA EN GESTIÓN DE AEROLÍNEAS
		print("------------------")
		print("GESTIÓN DE AEROLÍNEAS")
		print("------------------")
		print("a. Crear Aerolínea")
		print("b. Modificar Aerolínea")
		print("c. Eliminar Aerolínea")
		print("d. Volver")
		opcion2 = str(input("Elija una de las opciones indicando su letra "))
		while opcion2 != "a" and opcion2 != "b" and opcion2 != "c" and opcion2 != "d" :
			opcion2 = input("Elija una opción válida: ")

		if opcion2 == "d": #VOLVER
			print("------------------")
			print("Menú del administrador")
			print("------------------")
			print("1. Gestión de Aerolíneas")
			print("2. Aprobar/Denegar Promociones")
			print("3. Gestión de Novedades")
			print("4. Reportes")
			print("5. Salir")
			opcion = str(input("Elija una opción: "))

			while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion !="5":
				opcion = str(input("Elija una opción válida: "))

		if opcion2 == "a" : #CREAR AEROLÍNEA
			nombreAerolínea = str(input("Ingrese el nombre de la Aerolínea: "))
			codigoIATA = str(input("Ingrese el código IATA: "))
			while len(codigoIATA) != 3:
				codigoIATA = str(input("Ingrese un código IATA Válido: "))
			descripción = str(input("Ingrese una descripción: ")) #Falta el limite de caracteres
			codigoPais = str(input("Ingrese el código de país: "))
			while codigoPais != "ARG" and codigoPais != "CHI" and codigoPais != "BRA":
				codigoPais = str(input("Ingrese un código de país válido: "))
			codigoPais = codigoPais.upper()
			if codigoPais == "ARG":
				ARG = ARG + 1
			elif codigoPais == "BRA":
				BRA = BRA + 1 
			elif codigoPais == "CHI":
				CHI = CHI + 1
			#VER QUÉ PAÍS TIENE LA MAYOR CANTIDAD	
			if ARG >= BRA:
				if ARG > BRA:
					if ARG >= CHI:
						if ARG > CHI:
							print("ARG tiene más aerolíneas, con un total de:", ARG)
						else: #ARG = CHI
							print("ARG y CHI tienen más aerolíneas, con un total de:", ARG)
					else: #BRA<ARG<CHI
						print("CHI tiene más aerolíneas, con un total de:", CHI)
				else: #ARG=BRA
					if ARG >= CHI:
						if ARG > CHI:
							print("ARG y BRA tienen más aerolíneas, con un total de:", ARG)
						else: #ARG=CHI=BRA
							print("ARG,BRA y CHI tienen la misma cantidad de aerolíneas:", ARG)
					else: #ARG=BRA<CHI
						print("CHI tiene más aerolíneas, con un total de:", CHI)		
			else: #ARG<BRA
				if BRA >= CHI:
					if BRA > CHI:
						print("BRA tiene más aerolíneas, con un total de:", BRA)
					else: # ARG<BRA=CHI
						print("BRA y CHI tienen más aerolíneas, con un total de:", BRA)
				else: #ARG<BRA<CHI
					print("CHI tiene más aerolíneas, con un total de:", CHI)

			#VER QUÉ PAÍS TIENE LA MENOR CANTIDAD
			if ARG <= BRA:
				if ARG < BRA:
					if ARG <= CHI:
						if ARG < CHI:
							print("ARG tiene menos aerolíneas, con un total de:", ARG)
						else: #ARG=CHI
							print("ARG y CHI tienen menos aerolíneas, con un total de:", ARG)
					else: #CHI<ARG
						print("CHI tiene menos aerolíneas, con un total de:", CHI)
				else: #ARG=BRA
					if BRA <= CHI:
						if BRA < CHI:
							print("BRA y ARG tienen menos aerolíneas, con un total de:", BRA)
					else: #BRA>CHI
						print("CHI tiene menos aerolíneas, con un total de:", CHI)
			else: #ARG>BRA
				if BRA <= CHI:
					if BRA < CHI:
						print("BRA tiene menos aerolíneas, con un total de:", BRA)
					else: #BRA=CHI
						print("BRA y CHI tienen menos aerolíneas, con un total de:", BRA)
				else: #CHI<BRA
					print("CHI tiene menos aerolíneas, con un total de:", CHI)
					

		elif opcion2 == "b" :
			print("------------------")
			print("EN CONSTRUCCION")
			print("------------------")

		elif opcion2 == "c":
			print("------------------")
			print("EN CONSTRUCCION")
			print("------------------")


	elif opcion == "2" :
		print("------------------")
		print("EN CONSTRUCCION")
		print("------------------")

		print("------------------")
		print("Menú del administrador")
		print("------------------")
		print("1. Gestión de Aerolíneas")
		print("2. Aprobar/Denegar Promociones")
		print("3. Gestión de Novedades")
		print("4. Reportes")
		print("5. Salir")
		opcion = str(input("Elija una opción: "))

		while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion !="5":
			opcion = str(input("Elija una opción válida: "))


	elif opcion == "3" :
		print("------------------")
		print("GESTIÓN DE NOVEDADES")
		print("------------------")
		print("a. Crear Novedad")
		print("b. Modificar Novedad")
		print("c. Eliminar Novedad")
		print("d. Ver Novedades")
		print("e. Volver")
		opcion2 = str(input("Elija una de las opciones indicando su letra "))

		while opcion2 != "a" and opcion2 != "b" and opcion2 != "c" and opcion2 != "d" and opcion2 !="e":
			opcion2 = str(input("Elija una opción válida: "))

		if opcion2 == "a" or opcion2 == "c":
			print("------------------")
			print("EN CONSTRUCCION")
			print("------------------")

		elif opcion2 == "b":
			cod = input("Ingrese el código de la novedad que desea modificar: ")
			while cod != codNovedad1 and cod != codNovedad2 and cod != codNovedad3:
					cod = input("Ingrese un Código Válido: ")
			if cod == codNovedad1:
				textoNovedad1 = input("Ingrese la información:")
				fechaPublicacionNovedad1 = input("Ingrese la fecha de publicación: ")
				fechaExpiraciónNovedad1 = input("Ingrese la fecha de expiración: ")
			elif cod == codNovedad2:
				textoNovedad2 = input("Ingrese la información:")
				fechaPublicacionNovedad2 = input("Ingrese la fecha de publicación: ")
				fechaExpiraciónNovedad2 = input("Ingrese la fecha de expiración: ")
			elif cod == codNovedad3:
				textoNovedad3 = input("Ingrese la información:")
				fechaPublicacionNovedad3 = input("Ingrese la fecha de publicación: ")
				fechaExpiraciónNovedad3 = input("Ingrese la fecha de expiración: ")


		elif opcion2 == "d":
			print("---------------------------")
			print("Código del vuelo:",codNovedad1)
			print("Información:",textoNovedad1)
			print("Fecha de publicación:",fechaPublicacionNovedad1)
			print("Fecha de expiración:",fechaExpiraciónNovedad1)
			print("---------------------------")
			print("Código del vuelo:",codNovedad2)
			print("Información:",textoNovedad2)
			print("Fecha de publicación:",fechaPublicacionNovedad2)
			print("Fecha de expiración:",fechaExpiraciónNovedad2)
			print("----------------------------")
			print("Código del vuelo:",codNovedad3)
			print("Información:",textoNovedad3)
			print("Fecha de publicación:",fechaPublicacionNovedad3)
			print("Fecha de expiración:",fechaExpiraciónNovedad3)
			print("----------------------------")


		elif opcion2 == "e":
			print("------------------")
			print("Menú del administrador")
			print("------------------")
			print("1. Gestión de Aerolíneas")
			print("2. Aprobar/Denegar Promociones")
			print("3. Gestión de Novedades")
			print("4. Reportes")
			print("5. Salir")
			opcion = str(input("Elija una opción: "))

			while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion !="5":
				opcion = str(input("Elija una opción válida: "))


	elif opcion == "4":
		print("------------------")
		print("REPORTES")
		print("------------------")
		print("a. Reporte de Ventas(Reservas con estado 'Confirmada')")
		print("b. Reporte de Vuelos")
		print("c. Reporte de Usuarios")
		print("d. Volver")
		opcion2 = str(input("Elija una de las opciones indicando su letra "))
		if opcion2 == "d": #VOLVER
			print("Menú del administrador")
			print("------------------")
			print("1. Gestión de Aerolíneas")
			print("2. Aprobar/Denegar Promociones")
			print("3. Gestión de Novedades")
			print("4. Reportes")
			print("5. Salir")
			opcion = str(input("Elija una opción: "))

			while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion !="5":
				opcion = str(input("Elija una opción válida: "))

		elif opcion2 == "a" or opcion2 == "b" or opcion2 == "c" or opcion2 == "d":
			print("------------------")
			print("EN CONSTRUCCION")
			print("------------------")

if opcion == "5" :
	exit()
