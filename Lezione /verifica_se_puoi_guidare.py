#def controllo_patenti(età, patente):
età = int(input('Quanti anni hai?'))
if età >= 18:
    patente = input('Se hai la patente digita un asterisco altrimenti premi invio: ')
    if patente == "*":
        patente = True
        if patente == True:
            print("Puoi guidare la macchina!!!")
    elif not patente == "*":
        patente = False
        if patente == False:
            print("Non puoi guidare la macchina")
else:
    print ('Mi dispiace non puoi guidare la macchina sei troppo giovane!!!')
