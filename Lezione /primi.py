
#Per trovare un numero primo basta dividerlo per i numeri inferiori ad esso e contare i divisori. Se sono solo due, cioè 1 e se stesso, allora il numero è primo,
#altrimenti non lo è.

#Ma possiamo fare a meno di dividere per un numero più grande della sua metà, in quanto è scontato che darà sempre un numero con la virgola.

#Inoltre è scontato con un numero è divisibile quindi possiamo partire a dividere dal numero 2.
n = int(input('intervallo di numeri primi: '))


for conta in range (2,n+1):
  #  if not int(n) % conta == 0:
        for conta1 in range (n-1,conta,-1):
            print ("&", end=" ")
        print(" ")
        #if int(n) % conta == 0:
#            if print(conta) == 1:


