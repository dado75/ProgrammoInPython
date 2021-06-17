#Operazioni geometriche
while True:

    print('''
    Ciao e benvenuto. Calcola le aree dei poligoni!!!
    Creato da: Dado
    Scegli di quale poligono vuoi calcolare l'area:
    
    - Per calcolare l'area del rettangolo, seleziona 1;
    - Per calcolare l'area del triangolo, seleziona 2;
    - Per calcolare l'area del trapezio isoscele, seleziona 3;
    - Per calcolare l'area del cerchio, seleziona 4;
    - Per uscire dal programma digita ESC;
    ''')
    scegli = input("Inserisci il numero corrispondente all'operazione scelta --> ")
    if scegli == "1":
        print("Hai scelto di calcolare l'area del rettangolo:")
        b = float(input("Inserisci il valore della base del rettangolo in cm --> "))
        h = float(input("Inserisci il valore dell'altezza del rettangolo in cm --> "))
        if b < 0 or h < 0:
            print("valori errati")
        else:
            print("L'area del rettangolo è " + str(b * h) + ' cm2')
    elif scegli == "2":
        print("Hai scelto di calcolare l'area del tringolo rettangolo:")
        b = float(input("Inserisci il valore della base del tringolo rettangolo in cm --> "))
        h = float(input("Inserisci il valore della altezza del tringolo rettangolo in cm --> "))
        if b < 0 or h < 0:
            print("valori errati")
        else:
            print("L'area del tringolo rettangolo è " + str((b * h)/2) + ' cm2')
    elif scegli == "3":
        print("Hai scelto di calcolare l'area del trapezio isoscele:")
        bm = float(input("Inserisci il valore della base minore del trapezio isoscele in cm --> "))
        bM = float(input("Inserisci il valore della base maggiore del trapezio isoscele in cm --> "))
        h = float(input("Inserisci il valore dell'altezza del trapezio isoscele in cm --> "))
        if bm < 0 or bM < 0 or h < 0 or bm > bM:
            print("valori errati")
        else:
            print("L'area del trapezio isoscele è " + str((bm + bM * h) / 2) + ' cm2')
    elif scegli == "4":
        print("Hai scelto di calcolare l'area del cerchio:")
        r = float(input("Inserisci il raggio del cerchio in cm --> "))
        if r < 0:
            print("valori errati")
        else:
            print("L'area del cerchio è " + str(3.14 * r ** 2) + ' cm2')
    elif scegli == "ESC":
        print('''
        L'applicazione viene ora chiusa!! 
------------------------------------------------------------------------------------------------- ''')
        break
    loop = input("Desideri continuare ad utilizzare questa applicazione? S/N ")
    if loop == "S" or loop == "s" or loop == "yes" or loop == "YES":
        print('''Torno al menù principale!!!
-------------------------------------------------------------------------------------------------- ''')
    else:
        print('''Fine!
------------------------------------------------------------------------------------------------- ''')
        break