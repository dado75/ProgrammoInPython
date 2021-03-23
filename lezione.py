
#def controllo_patenti(età, patente):
    età = int(input('Quanti anni hai?'))
    patente = bool(input('Se hai la patente metti un asterisco: '))
    if età >= 18 and patente == True:
        print("Puoi guidare la macchina!!!")
    elif età >= 18 and patente == False:
        print("Non puoi guidare la macchina")
    else:
        print("Stai mentendo...")

