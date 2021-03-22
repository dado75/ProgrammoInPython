età = 12
diploma_scuola_media = True
if età >= 14 and diploma_scuola_media == True:
    print("Complimenti hai la licenza media")
elif età >= 14 and diploma_scuola_media == False:
    print("Sicuramente sei un ripetente")
elif età <= 14 and diploma_scuola_media == False:
    print("Studia ancora...")
else:
    print("Sei un genio!! oppure non me la racconti giusta...")