import getpass
import datetime
usuario = "a" #"admin@ventaspasajes777.com"
contraseña = "admin"
intentos = 0
cont_arg = 0
cont_chi = 0
cont_bra = 0
nov1, texto1, autor1, fecha1 = "1", "Demora en vuelo 105", "Milton", "25/03/2025"
nov2, texto2, autor2, fecha2 = "2", "Cancelación por clima", "Claudia", "07/02/2025"
nov3, texto3, autor3, fecha3 = "3", "Reprogramación servicio", "Claudia", "11/01/2025"



def AdOp():
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║                   Menu del administrado                   ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║1) Gestión de Aerolíneas                                   ║")
    print("║2) Aprobar/Denegar Promociones                             ║")
    print("║3) Gestión de Novedades                                    ║")
    print("║4) Reportes                                                ║")
    print("║0) Salir                                                   ║")
    print("╠═══════════════════════════════════════════════════════════╣")

def GAOp():
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║                   Gestión de Aerolíneas                   ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║1) Crear Aerolínea                                         ║")
    print("║2) Modificar Aerolínea                                     ║")
    print("║3) Eliminar Aerolínea                                      ║")
    print("║0) Volver                                                  ║")
    print("╠═══════════════════════════════════════════════════════════╣")

def GNOp():
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║                   Gestion de Novedades                    ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║1) Crear Novedad                                           ║")
    print("║2) Modificar Novedad                                       ║")
    print("║3) Eliminar Novedad                                        ║")
    print("║4) Ver Novedades                                           ║")
    print("║0) Volver                                                  ║")
    print("╠═══════════════════════════════════════════════════════════╣")

def ReOp():
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║                         Reportes                          ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║1) Reporte de Ventas (reservas confirmada)                 ║")
    print("║2) Reporte de Vuelos                                       ║")
    print("║3) Reporte de Usuarios                                     ║")
    print("║0) Volver                                                  ║")
    print("╠═══════════════════════════════════════════════════════════╣")

def Ingreso():
    op = getpass.getpass("╠═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═╣")
    espacios_totales = 55
    espacios_restantes = espacios_totales - len(op)
    linea = "║ >> " + op + (" " * espacios_restantes) + "║"
    print(linea)
    return op

def GestionAerolinea():
    GAOp()
    print("║                     Ingrese una opcion                    ║")
    op = Ingreso()
    while(op != "1" and op != "2" and op != "3" and op != "0"):
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║           Opcion invalida, ingreselo nuevamente           ║")
        op = Ingreso()
    match op:
        case "1": CrearAerolinea()
        case "2": EnConstruccion() #ModificarAerolinea
        case "3": EnConstruccion() #EliminarAerolinea
        case "0": 0 #Te devuelve al menu del administrador

def CrearAerolinea():
    global cont_arg, cont_chi, cont_bra
    rep = "S"
    while (rep == "S" or rep == "s"):
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║             Ingrese el nombre de la aerolínea             ║")
        nombrea = Ingreso()
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║         Ingrese el código IATA (max 3 caracteres)         ║")
        codiata = Ingreso()
        while (len(codiata) > 3):        
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                Error en el IATA, reintente                ║")
            codiata = Ingreso()
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║          Ingrese una descripcion de la aerolínea          ║")
        descra = Ingreso()
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║       Ingrese el código de un país (ARG, CHI o BRA)       ║")
        pais = Ingreso()
        while not (pais == "ARG" or pais == "CHI" or pais == "BRA" or pais == "arg" or pais == "chi" or pais == "bra"):        
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║     Código de país invalido o no existente, reintente     ║")
            pais = Ingreso()
        if pais == "ARG" or pais == "arg":
            cont_arg = cont_arg + 1
        elif pais == "CHI" or pais == "chi":
            cont_chi = cont_chi + 1
        elif pais == "BRA" or pais == "bra":
            cont_bra = cont_bra + 1
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║          ¿Quieres crear otra aerolinea? (S/N)             ║")
        rep = Ingreso()       
        while not (rep == "S" or rep == "s" or rep == "N" or rep == "n"):
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║          ¿Quieres crear otra aerolinea? (S/N)             ║")
            rep = Ingreso()
        if rep == "N" or rep == "n":
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                   Aerolineas cargadas                     ║")
            print("╠═══════════════════════════════════════════════════════════╣")
            if cont_arg >= cont_chi and cont_chi >= cont_bra:
                print("║                   ARG:", cont_arg,"CHI:", cont_chi,"BRA:", cont_bra,"                   ║")
            elif cont_bra >= cont_chi and cont_chi >= cont_arg:
                print("║                   BRA:", cont_bra,"CHI:", cont_chi,"ARG:", cont_arg,"                   ║")
            elif cont_arg >= cont_bra and cont_bra >= cont_chi:
                print("║                   ARG:", cont_arg,"BRA:", cont_bra,"CHI:", cont_chi,"                   ║")
            elif cont_bra >= cont_arg and cont_arg >= cont_chi:
                print("║                   BRA:", cont_bra,"ARG:", cont_arg,"CHI:", cont_chi,"                   ║")
            elif cont_chi >= cont_bra and cont_bra >= cont_arg:
                print("║                   CHI:", cont_chi,"BRA:", cont_bra,"ARG:", cont_arg,"                   ║")
            else:
                print("║                   CHI:", cont_chi,"ARG:", cont_arg,"BRA:", cont_bra,"                   ║")
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║     Ingrese (V) para volver al menu del administrador     ║")
            new = Ingreso()
            while new != "V" and new != "v":
                print("╠═══════════════════════════════════════════════════════════╣")
                print("║     Ingrese (V) para volver al menu del administrador     ║")
                new = Ingreso()
            #Te devuelve al menu del administrador


"""    new = input("¿Volver a Gestion Aer o Administrador? (1/2): ")
    while (new != "1" and new != "2"):
        new = input("¿Volver a Gestion Aer o Administrador? (1/2): ")
    if new == "1":
        GestionAerolinea()
    else:
        0"""

def GestionN():
    GNOp()
    print("║                   Seleccione una opcion                   ║")
    op = Ingreso()
    while(op != "1" and op != "2" and op != "3" and op != "4" and op != "0"):
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║           Opcion invalida, ingreselo nuevamente           ║")
        op = Ingreso()
    match op:
        case "1": EnConstruccion() #CrearNovedad()
        case "2": ModificarN()
        case "3": EnConstruccion() #EliminarNovedad()
        case "4": VerN()
        case "0": 0 #Te devuelve al menu del administrador

def VerN():
    global nov1
    global nov2
    global nov3
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║                         Novedades                         ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║ Codigo de Novedad:", nov1,"                                     ║")
    espacios_totales_text = 51
    espacios_restantes = espacios_totales_text - len(texto1)
    txtespacio1 = texto1 + (" " * espacios_restantes) + "║"
    print("║ Desc: ", txtespacio1)
    espacios_totales_autor = 50
    espacios_restantes = espacios_totales_autor - len(autor1)
    autorespacio1 = autor1 + (" " * espacios_restantes) + "║"  
    print("║ Autor: ", autorespacio1)
    print("║ Ultima modificacion: ", fecha1,"                         ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║ Codigo de Novedad:", nov2,"                                     ║")
    espacios_restantes = espacios_totales_text- len(texto2)
    txtespacio2 = texto2 + (" " * espacios_restantes) + "║"
    print("║ Desc: ", txtespacio2)
    espacios_restantes = espacios_totales_autor - len(autor2)
    autorespacio2 = autor2 + (" " * espacios_restantes) + "║"  
    print("║ Autor: ", autorespacio2)
    print("║ Ultima modificacion: ", fecha2,"                         ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║ Codigo de Novedad:", nov3,"                                     ║")
    espacios_restantes = espacios_totales_text - len(texto3)
    txtespacio3 = texto3 + (" " * espacios_restantes) + "║"
    print("║ Desc: ", txtespacio3)                 
    espacios_restantes = espacios_totales_autor - len(autor3)
    autorespacio3 = autor3 + (" " * espacios_restantes) + "║"  
    print("║ Autor: ", autorespacio3)
    print("║ Ultima modificacion:", fecha3,"                          ║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║     Ingrese (V) para volver al menu del administrador     ║")
    new = Ingreso()
    while new != "V" and new != "v":
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║     Ingrese (V) para volver al menu del administrador     ║")
        new = Ingreso()
    #Te devuelve al menu del administrador

"""    while True:
        new = input("¿Volver a Gestion Novedad o Administrador? (1/2): ")
        if new == "1":
            GestionN()
        elif new == "2":
            AdminMenu()"""

def ModificarN():
    global nov1, texto1, autor1, fecha1
    global nov2, texto2, autor2, fecha2
    global nov3, texto3, autor3, fecha3
    global fecha

    seguir = "s"
    while seguir == "s" or seguir == "S":
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║        Ingrese el codigo de la novedad a modificar        ║")
        mod = Ingreso()
        while (mod != "1" and mod != "2" and mod != "3"):
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║               Codigo invalido, reingresar                 ║")
            mod = Ingreso()

        if mod == nov1:
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                       Nuevo Texto                         ║")
            texto1 = Ingreso()
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                       Nuevo Autor                         ║")
            autor1 = Ingreso()
            fca = True
            while fca == True:
                try:
                    print("║        Ingrese una fecha con formato DD/MM/AAAA           ║")
                    fecha = Ingreso()
                    while (len(fecha) != 10):        
                        print("╠═══════════════════════════════════════════════════════════╣")
                        print("║                     Fecha invalida                        ║")
                        fecha = Ingreso()
                    datetime.datetime.strptime(fecha, '%d/%m/%Y')
                    print("╠═══════════════════════════════════════════════════════════╣")
                    print("║                   Novedad actualizada                     ║")
                    print("╠═══════════════════════════════════════════════════════════╣")
                    fca = False
                except ValueError:
                    print("╠═══════════════════════════════════════════════════════════╣")
                    print("║                     Fecha invalida                        ║")
                    print("╠═══════════════════════════════════════════════════════════╣")
            fecha1 = fecha

        elif mod == nov2:
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                       Nuevo Texto                         ║")
            texto2 = Ingreso()
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                       Nuevo Autor                         ║")
            autor2 = Ingreso()
            fca = True
            while fca == True:
                try:
                    print("║        Ingrese una fecha con formato DD/MM/AAAA           ║")
                    fecha = Ingreso()
                    while (len(fecha) != 10):        
                        print("╠═══════════════════════════════════════════════════════════╣")
                        print("║                     Fecha invalida                        ║")
                        fecha = Ingreso()
                    datetime.datetime.strptime(fecha, '%d/%m/%Y')
                    print("╠═══════════════════════════════════════════════════════════╣")
                    print("║                   Novedad actualizada                     ║")
                    print("╠═══════════════════════════════════════════════════════════╣")
                    fca = False
                except ValueError:
                    print("╠═══════════════════════════════════════════════════════════╣")
                    print("║                     Fecha invalida                        ║")
                    print("╠═══════════════════════════════════════════════════════════╣")
            fecha2 = fecha

        elif mod == nov3:
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                       Nuevo Texto                         ║")
            texto3 = Ingreso() 
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                       Nuevo Autor                         ║")
            autor3 = Ingreso()
            fca = True
            while fca == True:
                try:
                    print("║        Ingrese una fecha con formato DD/MM/AAAA           ║")
                    fecha = Ingreso()
                    while (len(fecha) != 10):        
                        print("╠═══════════════════════════════════════════════════════════╣")
                        print("║                     Fecha invalida                        ║")
                        fecha = Ingreso()
                    datetime.datetime.strptime(fecha, '%d/%m/%Y')
                    print("╠═══════════════════════════════════════════════════════════╣")
                    print("║                   Novedad actualizada                     ║")
                    print("╠═══════════════════════════════════════════════════════════╣")
                    fca = False
                except ValueError:
                    print("╠═══════════════════════════════════════════════════════════╣")
                    print("║                     Fecha invalida                        ║")
                    print("╠═══════════════════════════════════════════════════════════╣")
            fecha3 = fecha

        print("║         ¿Quieres modificar otra novedad? (S/N)            ║")
        rep = Ingreso()      
        while not (rep == "S" or rep == "s" or rep == "N" or rep == "n"):
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║         ¿Quieres modificar otra novedad? (S/N)            ║")
            rep = Ingreso()
        if rep == "N" or rep == "n":
            seguir = "N"
            #Te regresa al menu del administrador

"""def ValidarF():
    fca = True
    while fca == True:
        try:
            fecha = input ("Ingrese una fecha con formato YYYY/MM/DD:")
            datetime.datetime.strptime(fecha, "%Y%m/%d")
            print("-------------------")
            print("Novedad actualizada")
            print("-------------------")
            fca = False
        except ValueError:
            print ("Fecha invalida")
    fecha3 = fecha"""

def Reportes():
    ReOp()
    print("║                     Ingrese una opcion                    ║")
    op = Ingreso()
    while(op != "1" and op != "2" and op != "3" and op != "0"):
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║           Opcion invalida, ingreselo nuevamente           ║")
        op = Ingreso()
    match op:
        case "1": EnConstruccion() #Reporte de Ventas (reservas confirmada)
        case "2": EnConstruccion() #Reporte de Vuelos
        case "3": EnConstruccion() #Reporte de Usuarios
        case "0": 0 #Te devuelve al menu del administrador

def EnConstruccion():
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║<!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!║")
    print("║<!><!><!><!><!><!>En construcción...<!><!><!><!><!><!><!><!║")
    print("║<!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!><!║")
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║     Ingrese (V) para volver al menu del administrador     ║")
    new = Ingreso()
    while new != "V" and new != "v":
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║     Ingrese (V) para volver al menu del administrador     ║")
        new = Ingreso()
    #Te devuelve al menu del administrador

#Programa Principal
while (intentos != 3 and intentos !=4):
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║                     Ingrese el usuario                    ║")
    usin = Ingreso()
    print("╠═══════════════════════════════════════════════════════════╣")
    print("║                   Ingrese la contraseña                   ║")
    conin = getpass.getpass("╠═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═V═╣")
    print("║ >> x-x-x                                                  ║")
    if usin == usuario and conin == contraseña:
        intentos = 4
    elif intentos < 2:
        intentos = intentos + 1  
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║          Usuario o contraseña incorrecta",intentos,"/ 3            ║")
        print("╚═══════════════════════════════════════════════════════════╝")
    else:
        intentos = intentos + 1
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║   Alcanzo el limite de intentos 3/3, intente mas tarde    ║")
        print("╚═══════════════════════════════════════════════════════════╝")

while intentos == 4:
    AdOp()
    print("║                   Seleccione una opcion                   ║")
    op = Ingreso()
    while(op != "1" and op != "2" and op != "3" and op != "4" and op != "0"):
        print("╠═══════════════════════════════════════════════════════════╣")
        print("║           Opcion invalida, ingreselo nuevamente           ║")
        op = Ingreso()
    match op:
        case "1": GestionAerolinea()
        case "2": EnConstruccion()
        case "3": GestionN()
        case "4": Reportes()
        case "0":
            print("╠═══════════════════════════════════════════════════════════╣")
            print("║                Programa Finalizado, NV                    ║")
            print("╚═══════════════════════════════════════════════════════════╝")
            intentos = 5


    
"""
if intentos == 0:
    Verificacion()
elif acceso == True:                
    AdOp()
    op = str(input("Seleccione una opcion: "))
    while(op != "1" and op != "2" and op != "3" and op != "4" and op != "0"):
        op = str(input("Opcion invalida, ingreselo nuevamente: "))
    match op:
        case "1": GestionAerolinea()
        case "2": EnConstruccion()
        case "3": GestionN()
        case "4": EnConstruccion()
        case "0":
            print("-----------------------")
            print("Programa Finalizado, NV")
            print("-----------------------")"""
"""
intentos = 0
while (intentos != 3):
            usin = input("Ingrese el usuario: ")
            conin = getpass.getpass("Ingrese la contraseña: ")
            if usin == usuario and conin == contraseña:
                AdminMenu()

                
            else:
                print("-------------------------------")
                print("Usuario o contraseña incorrecta")
                print("-------------------------------")
                intentos = intentos + 1
if intentos == 3:
    print ("------------------------------------------------------")
    print ("Alcanzaste el limite de intentos (3), pruebe mas tarde")
    print ("------------------------------------------------------") """

"""
for intentos in range(3):
    usin = input("Ingrese el usuario: ")
    conin = getpass.getpass("Ingrese la contraseña: ")
    if usin == usuario and conin == contraseña:

    elif intentos < 2:
        intentos = intentos + 1
        print("------------------------------- ╔═══════╗")
        print("Usuario o contraseña incorrecta ║",intentos,"/ 3 ║")
        print("------------------------------- ╚═══════╝")
    else:
        print ("--------------------------------- ╔═══════╗ ----------------")
        print ("Alcanzaste el limite de intentos  ║ 3 / 3 ║, pruebe mas tarde")
        print ("--------------------------------- ╚═══════╝ -----------------")"""


