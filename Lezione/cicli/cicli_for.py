#for contatore in range(101):
#    print(contatore)

#for contatore in range(0,70,7):
#    print(contatore)

#for contatore in range(70,0,-7):
#    print(contatore)
#----------------------------
#while True:
#n = input('Trova i divisori di questo numero: ')
#for conta in range (2,int(n)):
#    if int(n) % conta == 0:
#        print(conta)
#----------------------------
#while True:
#    div = 2
#    count = 0
#    n = int(input('Trova i divisori di questo numero: '))
#    for conta in range (1,n+1):
        #if int(n) % conta == 0:
#            if print(conta) == 1:
#            if conta == (1,conta):
#                print(conta)



for n in range(2, 250):
    for x in range(2, n):
        if n % x == 0:
           # print(n, 'uguale', x, '*', n//x)
            break
    else:
#        print(n, 'è un numero primo')
        print(n)