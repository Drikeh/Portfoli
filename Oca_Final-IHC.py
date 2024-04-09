#"[·] Has caigut en un Dau [:]"
import random
import os
# Función para limpiar pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
# Función para mostrar el menú
def mostrarMenu():

    msg = "Benvingut al Joc de l'Oca!\nEscull una opció:\n1.Inicialitzar Joc\n"
    msg += "2.Visualitzar taulell \n3.Jugar\n0.Sortir" 
    print(msg)
    op = input("Entra un dels numeros del menu: ")
    while not op.isnumeric() or int(op) > 3 or int(op) < 0:
        limpiar_pantalla()
        op = input('\033[41m'+"Opció incorrecte!\n"+'\033[40m' + msg +"\nEntra un dels numeros del menu: ")
    return int(op)
# Función para generar el tablero
def generarTaulell():
    t = []
    oques = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
    # Formato de la casilla => |tttt ____ en total son 10 espacios
    for i in range(1, 64):
        if i in oques:
            t.append("|OCA      ")
        elif i == 26 or i == 53:
            t.append("|DAUS     ")
        elif i == 42:
            t.append("|LAB.     ")
        elif i == 58:
            t.append("|MORT     ")
        else:
            aux = " " if (i<10) else ""
            t.append(f"|{aux}{i}       ")
    return t
# Función para mostrar el tablero
def mostrarTaulell():
    if len(taulell) == 0:
        limpiar_pantalla()
        print('\033[41m'+"¡¡Per veure el taulell primer has de inicialitzar el Joc!!"+'\033[40m')
    else:    
        for x in range(len(taulell)):
            if x+1 in jugadors:
                # Poner la ficha del jugador que esté en esa casilla
                fitxs = ""
                k = 0
                for j in range(len(jugadors)):
                    if jugadors[j] == x+1:
                        fitxs += fitxes[j]
                        k+=1
                espais = (5 - k) * " "
                print(taulell[x][:5] + fitxs + espais, end="")
            else:
                print(taulell[x], end="")
            if x%14==0:
                print("|")
        print("|")
        return
# Función para inicializar las fichas de los jugadores
def inicialitzarFitxes():
    global fitxes
    negre = '\033[40m'
    vermell = '\033[41m'
    verd = '\033[42m'
    groc = '\033[43m'
    blau = '\033[44m'
    lila = '\033[45m'
    cyan = '\033[46m'
    gris = '\033[47m'

    fitxes = []
    fitxes.append(verd + " " + negre)
    fitxes.append(blau + " " + negre)
    fitxes.append(vermell + " " + negre)
    fitxes.append(groc + " " + negre)
    fitxes.append(lila + " " + negre)
    fitxes.append(cyan + " " + negre)
    fitxes.append(gris + " " + negre)
# Función para inicializar el juego
def inicialitzarJoc():
    inicialitzarFitxes()
    n = int(input("Indica quants jugadors sereu (2-6):"))
    limpiar_pantalla()
    global jugadors
    jugadors.clear()
    for i in range(n):
        jugadors.append(0)

    global taulell
    taulell.clear()
    taulell = generarTaulell()
    for i in range(n):
        print(fitxes[i], end="   ")
    print()
    return
# Función para jugar
def Jugar(tau):
    if len(jugadors) == 0:
        limpiar_pantalla()
        print('\033[41m'+"¡¡Per jugar primer has de inicialitzar el Joc!!"+'\033[040m')
    elif 63 in jugadors:
        limpiar_pantalla()
        print('\033[41m'+"¡¡La partida ja ha acabat¡Torna a inicialitzar el Joc!"+'\033[040m')
   
    else:
        limpiar_pantalla()
        partidaActiva = True
        torn = -1
        tir = 0
        while partidaActiva:
            # 1- Asignamos turno
            torn = (torn + 1) % len(jugadors)
            canviarTorn = False

            # 2- Bucle de tiradas hasta que cambiamos de turno o algún jugador llega a 63
            while not canviarTorn and jugadors[torn] < 63:
                tir += 1
                canviarTorn = ferTirada(tau, torn)
                mostrarTaulell()
                input("Prem return per continuar...")
                limpiar_pantalla()
            
            # 3- Si un jugador llega al final, se acaba la partida
            if jugadors[torn] == 63:
                limpiar_pantalla()
                partidaActiva = False
                print(f"Enhorabona jugador {torn+1}!! Has guanyat la partida!")
                print("██╗   ██╗██╗ █████╗ ████████╗ █████╗ ██████╗ ██╗ █████╗   ██████╗  █████╗ ██████╗  █████╗ ")
                print("██║   ██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
                print("╚██╗ ██╔╝██║██║  ╚═╝   ██║   ██║  ██║██████╔╝██║███████║  ██████╔╝███████║██████╔╝███████║")
                print(" ╚████╔╝ ██║██║  ██╗   ██║   ██║  ██║██╔══██╗██║██╔══██║  ██╔═══╝ ██╔══██║██╔══██╗██╔══██║")
                print("  ╚██╔╝  ██║╚█████╔╝   ██║   ╚█████╔╝██║  ██║██║██║  ██║  ██║     ██║  ██║██║  ██║██║  ██║")
                print("   ╚═╝   ╚═╝ ╚════╝    ╚═╝    ╚════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝")
                if torn==0:
                    print("     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ██████╗     ███╗  ")
                    print("     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗   ████║  ")
                    print("     ██║██║   ██║██║  ██╗ ███████║██║  ██║██║  ██║██████╔╝  ██╔██║  ")
                    print("██╗  ██║██║   ██║██║  ╚██╗██╔══██║██║  ██║██║  ██║██╔══██╗  ╚═╝██║  ")
                    print("╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚█████╔╝██║  ██║  ███████╗")
                    print(" ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝  ╚══════╝")
                elif torn==1:
                    print("     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ██████╗    █████╗  ")
                    print("     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██   ██║  ")
                    print("     ██║██║   ██║██║  ██╗ ███████║██║  ██║██║  ██║██████╔╝     ██║  ")
                    print("██╗  ██║██║   ██║██║  ╚██╗██╔══██║██║  ██║██║  ██║██╔══██╗   ██║  ")
                    print("╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚█████╔╝██║  ██║  ███████╗")
                    print(" ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝  ╚══════╝")
                elif torn==2:
                    print("     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ██████╗    █████╗  ")
                    print("     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██   ██║  ")
                    print("     ██║██║   ██║██║  ██╗ ███████║██║  ██║██║  ██║██████╔╝     ██║  ")
                    print("██╗  ██║██║   ██║██║  ╚██╗██╔══██║██║  ██║██║  ██║██╔══██╗  ██   ██║  ")
                    print("╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚█████╔╝██║  ██║   █████║")
                    print(" ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝   ╚════╝")
                elif torn==3:
                    print("     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ██████╗      ████╗")
                    print("     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗    ██ ██║")
                    print("     ██║██║   ██║██║  ██╗ ███████║██║  ██║██║  ██║██████╔╝   ██  ██║")
                    print("██╗  ██║██║   ██║██║  ╚██╗██╔══██║██║  ██║██║  ██║██╔══██╗  ███████║")
                    print("╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚█████╔╝██║  ██║       ██║")
                    print(" ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝       ╚═╝")
                elif torn==4:
                    print("     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ██████╗   ███████╗")
                    print("     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝")
                    print("     ██║██║   ██║██║  ██╗ ███████║██║  ██║██║  ██║██████╔╝  ███████╗")
                    print("██╗  ██║██║   ██║██║  ╚██╗██╔══██║██║  ██║██║  ██║██╔══██╗  ╚════██║")
                    print("╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚█████╔╝██║  ██║  ███████╗")
                    print(" ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝  ╚══════╝")
                else:
                    print("     ██╗██╗   ██╗ ██████╗  █████╗ ██████╗  █████╗ ██████╗   ███████╗")
                    print("     ██║██║   ██║██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝")
                    print("     ██║██║   ██║██║  ██╗ ███████║██║  ██║██║  ██║██████╔╝  ███████╗")
                    print("██╗  ██║██║   ██║██║  ╚██╗██╔══██║██║  ██║██║  ██║██╔══██╗  ██═══██║")
                    print("╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██████╔╝╚█████╔╝██║  ██║  ███████╗")
                    print(" ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝  ╚══════╝")                    
# Función para realizar una tirada
def ferTirada(tau, torn):
    # Tirar el dado
    tirada = random.randint(1, 6)
    print(f"El jugador {torn + 1} ha sacado un {tirada}!")
    
    # Incrementar la posición del jugador X
    jugadors[torn] += tirada
    
    # Límites del tablero
    if jugadors[torn] > 63:
        retroceso = jugadors[torn]- 63
        jugadors[torn] = 63-retroceso    
    elif jugadors[torn] < 1:
        jugadors[torn] = 1

    # Comprobar acciones adicionales de la tirada
    canviarTorn = comprovarAccionsTirada(tau, torn)
    
    return canviarTorn
# Función para comprobar las acciones tras una tirada
def comprovarAccionsTirada(tau, torn):
    casella = tau[jugadors[torn] - 1]
    if "OCA" in casella:
        # Encontrar la próxima casilla de "OCA" después de la actual
        siguiente_oca = None
        for i in range(jugadors[torn], len(tau)):
            if "OCA" in tau[i]:
                print('\033[94m'+"                                          "+'\033[0m')
                print('\033[94m'+"  █████╗  █████╗  █████╗            ███▄▄ "+'\033[0m')
                print('\033[94m'+" ██╔══██╗██╔══██╗██╔══██╗  ▄▄█████▄ ██▀   "+'\033[0m')
                print('\033[94m'+" ██║  ██║██║     ███████║ ██████▄██▄▀███  "+'\033[0m')
                print('\033[96m'+" ██║  ██║██║  ██╗██╔══██║   ▀██████████▀  "+'\033[0m')
                print('\033[96m'+" ╚█████╔╝╚█████╔╝██║  ██║      █▄█▄▄      "+'\033[0m')
                print('\033[96m'+"  ╚════╝  ╚════╝ ╚═╝  ╚═╝                 "+'\033[0m')
                print("El jugador",(torn+1), "ha caigut en OCA!!")
                print("Jugador", (torn+1), "torna a tirar")
                siguiente_oca = i
                break
        if siguiente_oca:
            # Teletransportar al jugador a la siguiente OCA
            jugadors[torn] = siguiente_oca + 1
            return False  # No hay cambio de turno, permitir al jugador tirar de nuevo
        else:
            return True  # Si no hay otra OCA, cambia de turno
        
    elif "DAUS" in casella:
        # Encontrar la otra casilla de "DAUS" en el tablero
        otra_daus = None
        for i in range(len(tau)):
            if "DAUS" in tau[i] and i != jugadors[torn] - 1:
                print("██████╗  █████╗ ██╗   ██╗███████╗    / O    /\\     ")
                print("██╔══██╗██╔══██╗██║   ██║██╔════╝   /   O  /O \\    ")
                print("██║  ██║███████║██║   ██║███████╗  /_____O/    \\   ")
                print("██║  ██║██╔══██║██║   ██║╚════██║  \\O    O\\    /  ")
                print("██████╔╝██║  ██║╚██████╔╝███████║   \\O    O\\ O/   ")
                print(" ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝    \\O____O\\/    ")
                print("El jugador",(torn+1), "ha caigut en els DAUS!!")
                otra_daus = i
                break
        
        if otra_daus:
            # Teletransportar al jugador a la otra casilla "DAUS"
            jugadors[torn] = otra_daus + 1
            return False  # No hay cambio de turno, permitir al jugador tirar de nuevo
        else:
            return True  # Si no hay otra casilla "DAUS", cambia de turno
        
    elif "LAB." in casella:
        # Desplazamiento a la casilla 30 con cambio de turno
        jugadors[torn] = 30
        print('\033[92m'+"██╗      █████╗ ██████╗ ███████╗██████╗ ██╗███╗  ██╗████████╗ ___________________________________    "+'\033[0m')
        print('\033[92m'+"██║     ██╔══██╗██╔══██ ██═════╝██╔══██╗██║████╗ ██║╚══██╔══╝ | _____ |   | ___ | _   ___ | |   |  | "+'\033[0m')
        print('\033[92m'+"██║     ███████║██████║ ███████╗██████╔╝██║██╔██╗██║   ██║    | |   | |_| |__ | |_|  _|____ | | |  | "+'\033[0m')
        print('\033[92m'+"██║     ██╔══██║██║  ██║██═════╝██╔══██╗██║██║╚████║   ██║    | | | |_________|__ |_____  |___| |  | "+'\033[0m')
        print('\033[93m'+"███████║██║  ██║██████╔╝███████╗██║  ██║██║██║ ╚███║   ██║    | |_|   _______   |____   ____|______| "+'\033[0m')
        print('\033[93m'+"╚══════╝╚═╝  ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚══╝   ╚═╝    |   __|_|_____|___________|___|______| "+'\033[0m')
        print("El jugador",(torn+1), "ha caigut al LABERINT!!")
        return True
    elif "MORT" in casella:
        # Desplazamiento a la casilla 1 con cambio de turno
        jugadors[torn] = 1
        print('\033[91m'" ███╗    ███╗ █████╗ ██████╗ ████████╗   _____"+'\033[0m')
        print('\033[91m'" ████║  ████║██╔══██╗██╔══██╗╚══██╔══╝  /    \\ "+'\033[0m')
        print('\033[91m'" ██║██╗██╔██║██║  ██║██████╔╝   ██║    | () () | "+'\033[0m')
        print('\033[91m'" ██║╚███╔╝██║██║  ██║██╔══██╗   ██║    \\  ^  /"+'\033[0m')
        print('\033[91m'" ██║ ╚█╔╝ ██║╚█████╔╝██║  ██║   ██║      ||||| "+'\033[0m')
        print('\033[91m'" ╚═╝  ╚╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝   ╚═╝      |||||"+'\033[0m')
        print("El jugador",(torn+1), "ha caigut a la MORT!!")
        print("Torna a començar")
        return True
    else:
        # Casilla numérica básica, cambio de turno
        return True

# Aquí comienza el main
# Declaración de variables
taulell = []
jugadors = []
fitxes = []
opcio = -1
# Bucle principal (que termina cuando el usuario elige "0- Salir")
while opcio != 0:
    # Llamada a la función para mostrar el Menú
    opcio = mostrarMenu()
    if opcio == 1:
        inicialitzarJoc()
        # print(taulell)
        mostrarTaulell()
    elif opcio == 2:
        mostrarTaulell()
    elif opcio == 3:
        Jugar(taulell)
#print(██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░██╗░█████╗░  ██████╗░░█████╗░██████╗░░█████╗░)
#print(██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗)
#print(╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝██║███████║  ██████╔╝███████║██████╔╝███████║)
#print(░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗██║██╔══██║  ██╔═══╝░██╔══██║██╔══██╗██╔══██║)
#print(░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║██║██║░░██║  ██║░░░░░██║░░██║██║░░██║██║░░██║)
#print(░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝)

#print(░░░░░██╗██╗░░░██╗░██████╗░░█████╗░██████╗░░█████╗░██████╗░  ░░███╗░░)
#print(░░░░░██║██║░░░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ░████║░░)
#print(░░░░░██║██║░░░██║██║░░██╗░███████║██║░░██║██║░░██║██████╔╝  ██╔██║░░)
#print(██╗░░██║██║░░░██║██║░░╚██╗██╔══██║██║░░██║██║░░██║██╔══██╗  ╚═╝██║░░)
#print(╚█████╔╝╚██████╔╝╚██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║  ███████╗)
#print(░╚════╝░░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝)
#print(███╗░░██╗██╗░█████╗░████████╗░█████╗░██████╗░██╗░█████╗░  ██████╗░░█████╗░██████╗░░█████╗░)
#print(████╗░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗)
#print(██╔██╗██║██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝██║███████║  ██████╔╝███████║██████╔╝███████║)
#print(██║╚████║██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗██║██╔══██║  ██╔══██╗██╔══██║██╔═══╝░██╔══██║)
#print(██║░╚███║██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║██║██║░░██║  ██║░░██║██║░░██║██║░░░░░██║░░██║)
#print(╚═╝░░╚══╝╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝)
 