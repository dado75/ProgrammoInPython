#def controllo_patenti(età, patente):


età = int(input('Quanti anni hai? '))
while età >= 18:
    patente = input('Bene sei maggiorenne!! Hai la patente? SI/NO: ')
    if patente == "SI" or patente == "si":
        #patente = True
        #if patente == True:
            print("Puoi nolleggiare la macchina!!!")
            break
    elif patente == "NO" or patente == "no":
        #patente = False
        #if patente == False:
            print("Non puoi noleggiare la macchina")
            break
    else:
        print("Hai usato un carattere non valido")
        continue
else:
    print ('Mi dispiace non puoi guidare la macchina sei troppo giovane!!!')
