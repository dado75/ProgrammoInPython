from funzioni_geometriche import*

# ciclone
# print(stampa_scelte())
while True:
    print(stampa_scelte())
    scegli = input("Inserisci il numero corrispondente all'area che vuoi calcolare --> ")
    if scegli == "1":
        area_rettangolo()
    elif scegli == "2":
        area_triangolo()
    elif scegli == "3":
        area_trapezio_iso()
    elif scegli == "4":
        area_cerchio()
    elif scegli == "ESC":
        print('''
                L'applicazione viene ora chiusa!! 
        ------------------------------------------------------------------------------------------------- ''')
        break
    loop = input("Desideri continuare ad utilizzare questa applicazione? S/N ")
    if loop == "S" or loop == "s":
        print('''Torno al menù principale!!!
    -------------------------------------------------------------------------------------------------- ''')
    else:
        print('''Fine!
    ------------------------------------------------------------------------------------------------- ''')
        break
 #   print(stampa_scelte())
 #   scegli = input("Inserisci il numero corrispondente all'operazione sceta --> ")