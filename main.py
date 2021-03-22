import csv
with open("./Mappa-delle-tabaccherie-in-Italia.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv,delimiter=";")
    header = next(lettore)
    print(header)
    Anno = input('Inserisci anno inserimento della tabaccheria: ')
    dati = [(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5], riga[6], riga[7], riga[8]) for riga in lettore if riga[4] == Anno]
    for tabaccheria in dati:
        print(f"{tabaccheria[:1]},{tabaccheria[:2]} -- Coordinate: {tabaccheria[8]},{tabaccheria[7]}")


