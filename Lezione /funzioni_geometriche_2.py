# definizione delle formule per calcolare le areee dei poligoni regolari

def stampa_scelte():
    return('''
            Ciao e benvenuto. Calcola le aree dei poligoni!!!
            Creato da: Dado
            Scegli di quale poligono vuoi calcolare l'area:

            - Per calcolare l'area del rettangolo, seleziona 1;
            - Per calcolare l'area del triangolo rettangolo, seleziona 2;
            - Per calcolare l'area del trapezio isoscele, seleziona 3;
            - Per calcolare l'area del cerchio, seleziona 4;
            - Per uscire dal programma digita ESC;
            ''')

def area_rettangolo(b,h):
    area = b * h
    return area

def area_triangolo(b,h):
    area = (b * h) / 2
    return area

def area_trapezio_iso(bm, bM, h):
    area = (bm+ bM * h) / 2
    return area

def area_cerchio(r):
    area = 3.14 * r ** 2
    return area