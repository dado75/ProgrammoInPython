# definizione delle formule per calcolare le areee dei poligoni regolari

def stampa_scelte():
    print ('''
            Ciao e benvenuto. Calcola le aree dei poligoni!!!
            Creato da: Dado
            Scegli di quale poligono vuoi calcolare l'area:
            
            - Per calcolare l'area del rettangolo, seleziona 1;
            - Per calcolare l'area del triangolo rettangolo, seleziona 2;
            - Per calcolare l'area del trapezio isoscele, seleziona 3;
            - Per calcolare l'area del cerchio, seleziona 4;
            - Per uscire dal programma digita ESC;
            ''')

def area_rettangolo ():
    print("Hai scelto di calcolare l'area del rettangolo:")
    b = float(input("Inserisci il valore della base del rettangolo in cm --> "))
    h = float(input("Inserisci il valore dell'altezza del rettangolo in cm --> "))
    if b < 0 or h < 0:
        print("valori errati")
    else:
        print("L'area del rettangolo è " + str(b * h) + ' cm2')

def area_triangolo ():
    print("Hai scelto di calcolare l'area del tringolo rettangolo:")
    b = float(input("Inserisci il valore della base del tringolo rettangolo in cm --> "))
    h = float(input("Inserisci il valore della altezza del tringolo rettangolo in cm --> "))
    if b < 0 or h < 0:
        print("valori errati")
    else:
        print("L'area del tringolo rettangolo è " + str((b * h) / 2) + ' cm2')

def area_trapezio_iso ():
    print("Hai scelto di calcolare l'area del trapezio isoscele:")
    bm = float(input("Inserisci il valore della base minore del trapezio isoscele in cm --> "))
    bM = float(input("Inserisci il valore della base maggiore del trapezio isoscele in cm --> "))
    h = float(input("Inserisci il valore dell'altezza del trapezio isoscele in cm --> "))
    if bm < 0 or bM < 0 or h < 0 or bm > bM:
        print("valori errati")
    else:
        print("L'area del trapezio isoscele è " + str((bm + bM * h) / 2) + ' cm2')

def area_cerchio ():
    print("Hai scelto di calcolare l'area del cerchio:")
    r = float(input("Inserisci il raggio del cerchio in cm --> "))
    if r < 0:
        print("valori errati")
    else:
        print("L'area del cerchio è " + str(3.14 * r ** 2) + ' cm2')