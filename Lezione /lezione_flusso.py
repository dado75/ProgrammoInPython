età = int(input('Quanti anni hai? '))
diploma_scuola_media = bool(input('Hai il diploma di scuola media? (se è vero metti un easterisco '))
if età >= 14 and diploma_scuola_media == True:
    print("Complimenti hai la licenza media")
elif età >= 14 and diploma_scuola_media == False:
    print("Sicuramente sei un ripetente")
elif età <= 14 and diploma_scuola_media == False:
    print("Studia ancora...")
else:
    print("Sei un genio!! oppure non me la racconti giusta...")