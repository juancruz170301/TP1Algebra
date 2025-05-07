import getpass

usuario = "admin@ventaspasajes777.com"
contraseña = "admin"
intentos = 0
cont_arg = 0
cont_chi = 0
cont_bra = 0
codigo1, texto1, autor1, fecha1 = 1, "Demora en vuelo 123", "Milton", "2024-03-01"
codigo2, texto2, autor2, fecha2 = 2, "Cancelación por clima", "Milton", "2024-05-20"
codigo3, texto3, autor3, fecha3 = 3, "Reprogramación servicio", "María", "2024-01-11"

def PreguntarDatos(intentos):
    if intentos == 3:
        print ("Demasiados intentos, intentalo más tarde")
        exit()
    us = input("Escriba su usuario: ")
    con = getpass.getpass("Escriba su contraseña: ")
    if us == usuario:
        if con == contraseña:
            MenuDelAdministrador()
        else:
            print("Usuario o contraseña Incorrectas")
            intentos +=1
            PreguntarDatos(intentos)
    else:
        print("Usuario o contraseña Incorrectas")
        intentos +=1
        PreguntarDatos(intentos)  

def GestionDeAerolineas():
    print ("-----------Gestión de Aerolíneas-----------")
    print ("")
    print ("a. Crear Aerolínea")
    print ("b. Modificar Aerolínea")
    print ("c. Eliminar Aerolínea")
    print ("d. Volver")
    print ("")
    while True:
        gestionaerolineasinput = input("Seleccione una opción ingresando su letra correspondiente: ")
        if gestionaerolineasinput == "a" or gestionaerolineasinput =="b" or gestionaerolineasinput == "c" or gestionaerolineasinput == "d":
            break
        else:
            print ("------------------------------")
            print ("Ingresa correctamente la letra")
            print ("------------------------------")

    if gestionaerolineasinput == "a":
        nombre = input("Ingresa el nombre de la aerolínea a crear: ")
        while True:
            codigoiata = input("Ingresar el código IATA (3 caracteres): ")
            if len(codigoiata) == 3 and type(codigoiata) == str:
                break
            else:
                print ("------------------------------------")
                print ("Ingresa correctamente el código IATA")
                print ("------------------------------------")

        descripcion = input("Ingresar una descripción: ")
        while True:
            codigopais = input ("Ingresar el codigo país (ARG, CHI, BRA): ")
            if codigopais == "ARG" or codigopais == "CHI" or codigopais == "BRA":
                break

            else:
                print ("-------------------------------------------------------")
                print ("Ingresa correctamente el codigo país entre las opciones")
                print ("-------------------------------------------------------")
        if codigopais == "ARG":
            global cont_arg
            cont_arg += 1
        elif codigopais == "CHI":
            global cont_chi
            cont_chi += 1
        elif codigopais == "BRA":
            global cont_bra
            cont_bra += 1

        if cont_arg > cont_chi:
            if cont_arg > cont_bra:
                print(f"Argentina es el país con más Aerolineas cargadas con un total de {cont_arg}")
            else:
                print(f"Brasil es el país con más Aerolineas cargadas con un total de {cont_bra}")
        elif cont_chi > cont_bra:
            print(f"Chile es el país con más Aerolineas cargadas con un total de {cont_chi}")
        else:
            print(f"Brasil es el país con más Aerolineas cargadas con un total de {cont_bra}")


        if cont_arg < cont_chi:
            if cont_arg < cont_bra:
                print(f"Argentina es el país con menos Aerolineas cargadas con un total de {cont_arg}")
            else:
                print(f"Brasil es el país con menos Aerolineas cargadas con un total de {cont_bra}")
        elif cont_chi < cont_bra:
            print(f"Chile es el país con menos Aerolineas cargadas con un total de {cont_chi}")
        else:
            print(f"Brasil es el país con menos Aerolineas cargadas con un total de {cont_bra}")


    elif gestionaerolineasinput == "b":
        print (">>>>>>>>>>>>>>>>>>")
        print ("En construcción...")
        print (">>>>>>>>>>>>>>>>>>")

    elif gestionaerolineasinput == "c":
        print (">>>>>>>>>>>>>>>>>>")
        print ("En construcción...")
        print (">>>>>>>>>>>>>>>>>>")

    elif gestionaerolineasinput == "d":
        MenuDelAdministrador()
    
    while True:
        regresar = input("Regresar al menu del Administrador?(S/N): ")
        if regresar =="S":
            MenuDelAdministrador()
        elif regresar == "N":
            exit()

def AprobarDenegarPromociones():
    print ("-----------Aprobar/Denegar Promociones-----------")

def GestionDeNovedades():
    print ("-----------Gestión De Novedades-----------")
    print ("")
    print ("a. Crear Novedad")
    print ("b. Editar Novedades")
    print ("c. Eliminar Novedad")
    print ("d. Ver Novedades")
    print ("e. Volver")
    print ("")
    
    while True:
        gestionnovedadesinput = input("Seleccione una opción ingresando su letra correspondiente: ")
        if gestionnovedadesinput == "a" or gestionnovedadesinput == "b" or gestionnovedadesinput ==  "c" or gestionnovedadesinput == "d" or gestionnovedadesinput == "e":
            break
        else:
            print ("------------------------------")
            print ("Ingresa correctamente la letra")
            print ("------------------------------")

    if gestionnovedadesinput == "a":
        print (">>>>>>>>>>>>>>>>>>")
        print ("En construcción...")
        print (">>>>>>>>>>>>>>>>>>")


    elif gestionnovedadesinput == "b":
        global codigo1, codigo2, codigo3
        while True:
            codigonum = int(input("Ingresá el código a editar: "))
            if codigonum == codigo1 or codigonum == codigo2 or codigonum == codigo3:
                break
            else:
                print ("-------------------------------")
                print ("Ingresa correctamente el codigo")
                print ("-------------------------------")
        
        if codigonum == codigo1:
            global texto1, autor1, fecha1
            texto1 = input("Nuevo texto: ")
            autor1 = input("Nuevo autor: ")
            fecha1 = input("Nueva fecha (YYYY-MM-DD): ")
            print ("Novedad Actualizada")
        
        elif codigonum == codigo2:
            global texto2, autor2, fecha2
            texto2 = input("Nuevo texto: ")
            autor2 = input("Nuevo autor: ")
            fecha2 = input("Nueva fecha (YYYY-MM-DD): ")
            print ("Novedad Actualizada")

        elif codigonum == codigo3:
            global texto3, autor3, fecha3
            texto3 = input("Nuevo texto: ")
            autor3 = input("Nuevo autor: ")
            fecha3 = input("Nueva fecha (YYYY-MM-DD): ")
            print ("Novedad Actualizada")


    elif gestionnovedadesinput == "c":
        print (">>>>>>>>>>>>>>>>>>")
        print ("En construcción...")
        print (">>>>>>>>>>>>>>>>>>")


    elif gestionnovedadesinput == "d":
        print ("-----------Novedades Cargadas-----------")
        print (f"Codigo de la novedad:{codigo1}")
        print (texto1)
        print (f"Autor: {autor1}")
        print (f"Fecha: {fecha1}")
        print ("----------------------------------------")
        print (f"Codigo de la novedad:{codigo2}")
        print (texto2)
        print (f"Autor: {autor2}")
        print (f"Fecha: {fecha2}")
        print ("----------------------------------------")
        print (f"Codigo de la novedad:{codigo3}")
        print (texto3)
        print (f"Autor: {autor3}")
        print (f"Fecha: {fecha3}")
        print ("----------------------------------------")


    elif gestionnovedadesinput == "e":
        MenuDelAdministrador()
    
    while True:
        regresar = input("Regresar al menu del Administrador?(S/N): ")
        if regresar =="S":
            MenuDelAdministrador()
        elif regresar == "N":
            exit()
        else:
            print ("-----------------------------------")
            print ("Ingresa correctamente si o no (S/N)")
            print ("-----------------------------------")


def Reportes():
    print ("-----------Reportes-----------")
    print ("")
    print ("a. Reporte de Ventas")
    print ("b. Reporte de Vuelos")
    print ("c. Reporte de Usuarios")
    print ("d. Volver")
    print ("")
    while True:
        gestionreportesinput = input("Seleccione una opción ingresando su letra correspondiente: ")
        if gestionreportesinput == "a" or gestionreportesinput == "b" or gestionreportesinput == "c" or gestionreportesinput == "d":
            break
        else:
            print ("------------------------------")
            print ("Ingresa correctamente la letra")
            print ("------------------------------")


    if gestionreportesinput == "a":
        print (">>>>>>>>>>>>>>>>>>")
        print ("En construcción...")
        print (">>>>>>>>>>>>>>>>>>")


    elif gestionreportesinput == "b":
        print (">>>>>>>>>>>>>>>>>>")
        print ("En construcción...")
        print (">>>>>>>>>>>>>>>>>>")


    elif gestionreportesinput == "c":
        print (">>>>>>>>>>>>>>>>>>")
        print ("En construcción...")
        print (">>>>>>>>>>>>>>>>>>")


    elif gestionreportesinput == "d":
        MenuDelAdministrador()

    else:
        while True:
            regresar = input("Regresar al menu del Administrador?(S/N): ")
            if regresar =="S":
                MenuDelAdministrador()
            elif regresar == "N":
                exit()
            else:
                print ("-----------------------------------")
                print ("Ingresa correctamente si o no (S/N)")
                print ("-----------------------------------")
        


def MenuDelAdministrador():
    print ("-----------Menú del Administrador-----------")
    print ("")
    print ("1. Gestión de Aerolíneas")
    print ("2. Aprobar/Denegar Promociones")
    print ("3. Gestión de Novedades")
    print ("4. Reportes")
    print ("5. Salir")
    print ("")
    while True:
        menudeladministradorinput = int(input("Seleccione una opción ingresando su número correspondiente: "))
        if menudeladministradorinput >= 1 and menudeladministradorinput <= 5:
            break
        else:
            print ("--------------------------------------------------")
            print ("Ingresa correctamente el número entre las opciones")
            print ("--------------------------------------------------")

    if menudeladministradorinput == 1:
        GestionDeAerolineas()

    if menudeladministradorinput == 2:
        AprobarDenegarPromociones()

    if menudeladministradorinput == 3:
        GestionDeNovedades()

    if menudeladministradorinput == 4:
        Reportes()

    if menudeladministradorinput == 5:
        print ("Saliendo del Sistema...")
        exit()


if PreguntarDatos(intentos) == True:
    MenuDelAdministrador()