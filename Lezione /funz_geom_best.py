#
"""
def print_options():
    print ("Options:")
    print (" 'p' print options")
    print (" 'c' convert from celsius")
    print (" 'f' convert from fahrenheit")
    print (" 'q' quit the program")

def celsius_to_fahrenheit(c_temp):
    return 9.0/5.0*c_temp+32

def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0)*5.0/9.0

choice = "p"
while choice != "q":
    if choice == "c":
        temp = float(input("Celsius temperature: "))
        print ("Fahrenheit:",celsius_to_fahrenheit(temp))
    elif choice == "f":
        temp = float(input("Fahrenheit temperature:"))
        print ("Celsius:",fahrenheit_to_celsius(temp))
    elif choice != "q":
        print_options()
    choice = input("option: ") """

from funzioni_geometriche import*

# ciclone
scegli = "p"
while scegli != "ESC":
  #  print(stampa_scelte())
    scegli = input("Inserisci il numero corrispondente all'operazione sceta --> ")
    if scegli == "1":
        area_rettangolo()
    elif scegli == "2":
        area_triangolo()
    elif scegli == "3":
        area_trapezio_iso()
    elif scegli == "4":
        area_cerchio()
    elif scegli != "ESC":
        loop = input("Desideri continuare ad utilizzare questa applicazione? S/N ")
        if loop == "S" or loop == "s":
            print(stampa_scelte())
    else:
        print('''Fine!
    ------------------------------------------------------------------------------------------------- ''')
    break
