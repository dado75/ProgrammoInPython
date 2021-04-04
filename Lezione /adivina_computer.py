count = 0
n = 9999999
r = 0

min = int(input("iNSERISCI IL MINIMO DEL DOMINIO DI SCELTA: "))
max = int(input("iNSERISCI IL MASSIMO DEL DOMINIO DI SCELTA: "))

while n != 0:
    count += 1

    r = min + ((max - min) // 2)

    print("Scelgo il numero ",r)

    print("  Se ho indovinato inserisci 0")
    print("  Se il tuo numero è superiore a ", r,"inserisci 1")
    print("  Se il tuo numero è inferire a ", r, "inserisci 2")

    n = int(input())

    if n == 1:
        min = r
    elif n == 2:
        max = r
    else:
        print("Ho indovinato in", count, "tentativi.")

