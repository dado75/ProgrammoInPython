from funz_operaz import*
#import funz_operaz
while True:
    print('''
    Calcolatrice:
    Digita + , - , * , /
    Per scegliere l'operazione da eseguire
    Oppure scrivi ESC per uscire
    ''')
    operazione = input("Inserisci il simbolo dell'operazione: ")
    if operazione == "+":
        num1 = int(input())
        num2 = int(input())
        print("La somma è:", somma(num1, num2))
    elif operazione == "-":
        num1 = int(input())
        num2 = int(input())
        print("La sottrazione è:", sottrazione(num1, num2))
    elif operazione == "*":
        num1 = int(input())
        num2 = int(input())
        print("La moltiplicazione è:", moltiplicazione(num1, num2))
    elif operazione == "/":
        num1 = int(input())
        num2 = int(input())
        print("La divisione è:", divisione(num1, num2))
    elif operazione == "ESC":
        print('Arrivederci!!!')
        break
    loop = input('Vuoi continuare ad usare la calcolatrice? S/N ')
    if loop == 'S' or loop == 's':
        print('Torno al menù!!')
    else:
        print('Fine!!!')
        break
else:
    print("Hai sbagliato operatore")
