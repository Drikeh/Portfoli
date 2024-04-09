#from random import randrange
from random import randint
def mostrarMenu():
	msg = "Benvingut al Joc de l'Oca!\nEscull una opció:\n1.Inicialitzar Joc\n"
	msg +="2.Visualitzar taulell \n3.Jugar\n0.Sortir" 
	print(msg)
	op = input()
	while not op.isnumeric() or int(op) > 3 or int(op) < 0:
		op = input('\033[41m'+"Opció incorrecte!"+'\033[40m' + msg)
	return int(op)


def generarTaulell():
	t = []
	oques = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
	# Format de la casella => |tttt ____ en total són 10 espais
	for i in range(1, 64):
		if i in oques:
			t.append("| OCA     ")
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


def inicialitzarJoc():
	inicialitzarFitxes()
	n = int(input("Indica quants jugadors sereu (2-6):"))
	##################
	global jugadors
	jugadors.clear()
	for i in range(n):
		jugadors.append(1)
#		jugadors.append(i+3)
	##################
	global taulell
	taulell.clear()
	taulell = generarTaulell()
	for i in range(n):
		print(fitxes[i], end="   ")
	print()
	return


def mostrarTaulell():
    for i in range(len(taulell)):
        if i+1 in jugadors:
            #Cal posar la fitxa del jugador que hi hagi
            fitxs = ""
            k = 0
            for j in range(len(jugadors)):
                if jugadors[j] == i+1:
                    fitxs += fitxes[j]
                    k+=1
            espais = (5 - k) * " "
            print(taulell[i][:5] + fitxs + espais, end="")
        else:
            print(taulell[i], end="")
        if i%12==0:
            print("|")
    print("|")
    return

# COMPLETA LA CAPÇALERA DE LA FUNCIÓ AMB ELS PARÀMETRES CORRESPONENTS
def ferTirada(jugador):
    # 1- Tirar el dau
	Tirada=randint(1,6)
    nova_posicio= (jugador[torn])+(Tirada)

    # 2- Recalcular posició
    # 	ATENCIÓ, cal controlar el REBOT

    # 3- Comprovar accions a fer. És una Funció() que retorna si S'HA de canviar de Torn o no, i li passem el taulell i el torn.






# Aquesta funció ens servirà per comprovar quines accions extres cal fer si hem caigut a la casella dels DAUS, de la MORT, del
#	 *  LABERINT, o en alguna OCA (amb especial atenció a la última OCA que et porta a la victòria). O si és una casella sense acció.
#	 * 	També controla quan hem de canviar el torn.
# COMPLETA LA CAPÇALERA DE LA FUNCIÓ AMB ELS PARÀMETRES CORRESPONENTS
def comprovarAccionsTirada():
    # Fixar-se en la casella on ha caigut el jugador “Torn”, si és numèrica bàsica O bé, si és una casella complexa 
    # 1- Controlar si cal fer un desplaçament o no.
    # 2- Controlar si cal fer canvi de torn o no.
    # RETORNA un booleà que indica a la funció FerTirada() si cal fer un canvi de torn o no
    oques=[5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
    
        
    if nova_posicio in oques and nova_posicio!=59 :
        print(f"El jugador ha arribat a la casella {nova_posicio}, ha caigut en una OCA!")
        oca=oques.index(nova_posicio) + 1
        nova_posicio=oques[oca]
        tirada = ferTirada()  
        nova_posicio += tirada  
    elif nova_posicio == 59:
        tirada = ferTirada()
        nova_posicio = (63 - tirada)
    elif nova_posicio == 26 or nova_posicio == 53:
        print(f"El jugador ha arribat a la casella {nova_posicio}, ha caigut en DAUS!")
        if nova_posicio==26:
            nova_posicio = 53
            tirada = ferTirada()  
            nova_posicio += tirada
        else:
            nova_posicio = 26
            tirada = ferTirada()  
            nova_posicio += tirada
        
    elif nova_posicio == 42:
        print(f"El jugador ha arribat a la casella {nova_posicio}, ha caigut en el LABERINT!")
        nova_posicio = 30  
        
    elif nova_posicio == 58:
        print(f"El jugador ha arribat a la casella {nova_posicio}, ha caigut en la MORT!")
        nova_posicio = 1  
    if nova_posicio > 63:
        nova_posicio = 63 - tirada  
    else:
        nova_posicio = (jugadors[torn])+(tirada)
        
    return nova_posicio 


def Jugar(taulell): 
    global jugadors
    torn = 0
    jugador = 0
   
    while True :    
        input(f"Jugador {torn + 1}, presiona Enter per tirar el dau...")  
        tirada = ferTirada()
        print(f"El jugador {torn+1} ha tirat un {tirada}")
        taulell[jugadors[torn]-1]=taulell[jugadors[torn]-1].replace(fitxes[torn],"")
        jugador = comprovarAccionsTirada(tirada, torn)
        print(comprovarAccionsTirada(tirada, torn))
        
        jugadors[torn]=jugador
        if 63 in jugadors :
            print(f"El jugador {torn + 1} ha guanyat!")
            break
        
        taulell[jugador-1] = f"{taulell[jugador-1]}     {fitxes[torn]}"
        mostraTaulell(taulell)
        torn = (torn + 1) % len(jugadors)
        print(jugadors)

	return 



def Jugar(tau):
    partidaActiva = True
    torn = -1
    tir = 0
    while partidaActiva:
        # 1- Assignem torn 
        torn = (torn +1 ) % len(jugadors)
        canviarTorn = False

        # 2- Bucle de tirades fins que canviem de torn o algun jugador arribi a 63
        while not canviarTorn and jugadors[torn] < 63:
            tir+=1
            canviarTorn = ferTirada(tau, torn)
            mostrarTaulell()
            input("Prem return per continuar...")
	
        # 3- Si un jugador arriba al final, s'acaba la partida
        if jugadors[torn] == 63:
            partidaActiva = False
            print(f"Enhorabona jugador {torn+1}!! Has guanyat la partida!")
        


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
    
    
# Aquí comença el main
# Declaració de variables
taulell = []
jugadors = []
fitxes = []
opcio = -1
# Bucle principal (que acaba quan l’usuari escull “0- Sortir”)
while opcio != 0:
	# Crida a la funció de mostrar Menú
	opcio = mostrarMenu()
	if opcio == 1:
		inicialitzarJoc()
		# print(taulell)
		mostrarTaulell()
	elif opcio == 2:
		mostrarTaulell()
	elif opcio == 3:
		Jugar(taulell)
	