#contatore = 0
#while contatore <= 100:
#    print(contatore)
#    contatore += 1

#for contatore in range(101):
#    print(contatore)

#for contatore in range(0,81,8):
#    print(contatore)

#for contatore in range(70,0,-7):
#    print(contatore)

n = input('Trova i non divisori di questo numero: ')
for conta in range (2,int(n)):
    if not int(n) % conta == 0:
        print(conta)
