import getpass
import datetime

usuario_co = "." #admin@ventaspasajes777.com 
contraseña_co = "admin"
intentos = 0

argv = 0
chiv = 0
brav = 0

codnov1, textnov1, autornov1, fechanov1 = "1", "Vuelo demorado", "Claudia", "10/04/2025"
codnov2, textnov2, autornov2, fechanov2 = "2", "Vuelo suspendido", "Claudia", "24/03/2025"
codnov3, textnov3, autornov3, fechanov3 = "3", "Cancelacion por clima", "Milton", "06/01/2025"

#TODOS LOS MENUS
def adminmenu():
    print("╔══════════════════════════════════╗")
    print("║          MENU PRINCIPAL          ║")
    print("╠══════════════════════════════════╣")
    print("║ 1) Gestion de Aerolíneas         ║")
    print("║ 2) Aprobar/Denegar Promociones   ║")
    print("║ 3) Gestión de Novedades          ║")
    print("║ 4) Reportes                      ║")
    print("║ 0) Volver                        ║")
    print("╚══════════════════════════════════╝")

def aerolineasmenu():
    print("╔══════════════════════════════════╗")
    print("║       Gestion de Aerolíneas      ║")
    print("╠══════════════════════════════════╣")
    print("║ 1) Crear Aerolínea               ║")
    print("║ 2) Modificar Aerolínea           ║")
    print("║ 3) Eliminar Aerolínea            ║")
    print("║ 0) Volver                        ║")
    print("╚══════════════════════════════════╝")
        
def novedadesmenu():
    print("╔══════════════════════════════════╗")
    print("║       Gestión de Novedades       ║")
    print("╠══════════════════════════════════╣")
    print("║ 1) Crear Novedad                 ║")
    print("║ 2) Modificar Novedad             ║")
    print("║ 3) Ver Novedades                 ║")
    print("║ 0) Volver                        ║")
    print("╚══════════════════════════════════╝")

def contruccion():
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒ EN CONSTRUCCIÓN... ▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print(" <Ingrese (V) para volver al menu>  ")
    volver = input("» ")
    while volver != "V" and volver != "v":
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("  <Ingrese (V) para volver al menu>  ")
        volver = input("» ")
    #VUELVE AL MENU PRINCIPAL

#CONTROL

def operaraAerolinea():
    aerolineasmenu()
    operar = (input("Selecciona una opción: ")) 
    while (operar != "1" and operar != "2" and operar != "3" and operar != "4" and operar != "0"):
            print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
            operar = (input("Seleccion invalida, ingrese denuevo: "))
    match operar:
        case "1": crearaero()
        case "2": contruccion()
        case "3": contruccion()
        case "0": 0 #volver 

def crearaero():
    global argv, chiv, brav, volver 
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    nombre = input("Ingrese un nombre para la Aerolínea: ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    iata = input("Ingrese el codigo IATA (max 3 caracteres): ")
    while (len(iata) > 3):
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        iata = input("Codigo mal colocado, ingrese denuevo: ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    desc = input("Ingrese una descripcion: ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    codpais = input("Ingrese su codigo de pais (ARG, CHI, BRA): ")
    while codpais != "ARG" and codpais != "arg" and codpais != "CHI" and codpais != "chi" and codpais != "BRA"  and codpais != "bra":         
       print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
       codpais = input("Codigo mal colocado, ingrese denuevo: ")
    if codpais == "ARG" or codpais == "arg":
        argv = argv + 1 
    elif codpais == "CHI" or codpais == "chi":
        chiv = chiv + 1
    elif codpais == "BRA" or codpais == "bra":
        brav = brav + 1
    #QUE PAIS TIENE MÁS
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print("               Aerolíneas subidas               ")
    print("")
    if argv >= chiv and chiv >= brav:
        print("            ARG:",argv,   "  CHI:",chiv,   "   BRA:",brav)
    elif argv >= brav and brav >= chiv:
        print("            ARG:",argv,   "  BRA:",brav,   "   CHI:",chiv)
    elif brav >= argv and argv >= chiv:
        print("            BRA:",brav,   "  ARG:",argv,   "   CHI:",chiv)
    elif brav >= chiv and chiv >= argv:
        print("            BRA:",brav,   "  CHI:",chiv,   "   ARG:",argv)
    elif chiv >= argv and argv >= brav:
        print("            CHI:",chiv,   "  ARG:",argv,   "   BRA:",brav)
    else:
        print("            CHI:",chiv,   "  BRA:",brav,    "   ARG:",argv)
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print(" <Ingrese (V) para volver al menu>  ")
    volver = input("» ")
    while volver != "V" and volver != "v":
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("  <Ingrese (V) para volver al menu>  ")
        volver = input("» ")

def Operarnovedades():
    novedadesmenu()
    operar = (input("Selecciona una opción: ")) 
    while (operar != "1" and operar != "2" and operar != "3" and operar != "4" and operar != "0"):
            print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
            operar = (input("Seleccion invalida, ingrese denuevo: "))
    match operar:
        case "1": contruccion()
        case "2": modificarnov()
        case "3": vernove()
        case "0": 0 #volver 
    
def modificarnov():
    global codnov1, codnov2, codnov3, textnov1, textnov2, textnov3, autornov1, autornov2, autornov3, fechanov1, fechanov2, fechanov3
    
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    codnov1 = input("Escriba el codigo de la novidad correspondiente: ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    textnov1 = input("Escriba una nueva descripcion: ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    autornov1 = input("Escriba modifique el autor: ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    fechanov1 = input("Ingrese una fecha (DD/MM/AAAA): ")
    fechanov1 = input("Error, ingrese denuevo: ")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print(" <Ingrese (V) para volver al menu>  ")
    volver = input("» ")
    while volver != "V" and volver != "v":
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("  <Ingrese (V) para volver al menu>  ")
        volver = input("» ")

def vernove():
    global codnov1, codnov2, codnov3
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                        NOVEDADES                         ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║ Codigo de novedad:",codnov1,                               )
    print("║ Descripcion:",textnov1,                                    )
    print("║ Autor:",autornov1,                                         )
    print("║ Fecha:",fechanov1,                                         ) 
    print("╠══════════════════════════════════════════════════════════╣")
    print("║ Codigo de novedad:",codnov2,                               )
    print("║ Descripcion:",textnov2,                                    )
    print("║ Autor:",autornov2,                                         )
    print("║ Fecha:",fechanov2,                                         ) 
    print("╠══════════════════════════════════════════════════════════╣")
    print("║ Codigo de novedad:",codnov3,                               )
    print("║ Descripcion:",textnov3,                                    )
    print("║ Autor:",autornov3,                                         )
    print("║ Fecha:",fechanov3,                                         )
    print("╚══════════════════════════════════════════════════════════╝")
    print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
    print(" <Ingrese (V) para volver al menu>  ")
    volver = input("» ")
    while volver != "V" and volver != "v":
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("  <Ingrese (V) para volver al menu>  ")
        volver = input("» ")

#INICIO DE SESIÓN
while (intentos != 3 and intentos != 4):
    print("Ingrese su usurario:")
    usuario = input("» ")
    print("Ingrese la contraseña:")
    contraseña = getpass.getpass("» ")
    if usuario == usuario_co and contraseña == contraseña_co:
        intentos = 4
    elif intentos < 2: 
        intentos = intentos + 1
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("≡ Usuario o contreseña incorrecta" "(",intentos,"/ 3 )≡")
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")    
    else:
        intentos = intentos + 1    
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
        print("≡ Demasiados intentos ( 3 / 3 ), cerrando programa... ≡")
        print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
#MENU PRINCIPAL 
while intentos == 4:
    adminmenu()
    operar = (input("Selecciona una opción: "))   
    while (operar != "1" and operar != "2" and operar != "3" and operar != "4" and operar != "0"):
            print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
            operar = (input("Seleccion invalida, ingrese denuevo: "))
    match operar:
        case "1": operaraAerolinea()
        case "2": contruccion()
        case "3": Operarnovedades()
        case "4": contruccion()
        case "0": 
            print("Cerrando programa...")
            intentos = 5