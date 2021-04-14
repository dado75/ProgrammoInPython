from funzioni_geometriche_2 import*

# ciclone
# print(stampa_scelte())
while True:
    print(stampa_scelte())
    scegli = input("Inserisci il numero corrispondente all'area che vuoi calcolare --> ")
    if scegli == "1":
        print("Hai scelto di calcolare l'area del rettangolo:")
        base = float(input("Inserisci il valore della base del rettangolo in cm --> "))
        altezza = float(input("Inserisci il valore dell'altezza del rettangolo in cm --> "))
        if base < 0 or altezza < 0:
            print("valori errati")
        else:
            print("L'area del rettangolo è ", area_rettangolo(base, altezza), ' cm2' )
    elif scegli == "2":
        print("Hai scelto di calcolare l'area del trinagolo rettangolo:")
        base = float(input("Inserisci il valore della base del triangolo rettangolo in cm --> "))
        altezza = float(input("Inserisci il valore dell'altezza del triangolo rettangolo in cm --> "))
        if base < 0 or altezza < 0:
            print("valori errati")
        else:
            print("L'area del trinagolo rettangolo è ", area_triangolo(base, altezza), ' cm2')
    elif scegli == "3":
        print("Hai scelto di calcolare l'area del trapezio isoscele:")
        basemin = float(input("Inserisci il valore della base minore del trapezio isoscele in cm --> "))
        basemagg = float(input("Inserisci il valore della base maggiore del trapezio isoscele in cm --> "))
        altezza = float(input("Inserisci il valore dell'altezza del trapezio isoscele in cm --> "))
        if basemin < 0 or basemagg < 0 or altezza < 0 or basemin > basemagg:
            print("valori errati")
        else:
            print("L'area del trapezio isoscele è " , area_trapezio_iso(basemin, basemagg, altezza), ' cm2')
    elif scegli == "4":
        print("Hai scelto di calcolare l'area del cerchio:")
        raggio = float(input("Inserisci il raggio del cerchio in cm --> "))
        if raggio < 0:
            print("valori errati")
        else:
            print ("L'area del cerchio è " , area_cerchio(raggio) , 'cm2')
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