import random

count = 0
n = 0
r = 0

min = int(input("iNSERISCI IL MINIMO DEL DOMINIO DI SCELTA: "))
max = int(input("iNSERISCI IL MASSIMO DEL DOMINIO DI SCELTA: "))

n = random.randint(min, max)

while n != r:
    count += 1
    r = int(input("Inserisci il numero da divinare: "))
    if r < n:
        print("il tuo numero è inferiore di quello scelto dal computer")
    elif r > n:
        print("il tuo numero è maggiore di quello scelto dal computer")
    else:
        print("Hai indovinato in" , count, "tentativi!!!")
