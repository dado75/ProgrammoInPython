import string
#import numpy as np
#from matplotlib import pyplot as plt

# apro il file di testo
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File connot be opened:' , fname)
    exit()

counts = dict()
for pippo in fhand:
    #elimino i caratteri a capo (chr10,chr13)
    pippo = pippo.rstrip()
    #elimino la punteggiatura
    pippo = pippo.translate(pippo.maketrans('', '', string.punctuation))
    #porto tutto minuscolo
    pippo = pippo.lower()
    #separo le parole e creo una lista di parole
    words = pippo.split()
    for word in words:
    #    if word not in counts:
    #        counts[word] = 1
    #    else:
    #        counts[word] += 1
        counts[word] = counts.get(word, 0) + 1

#print(counts)

lst = sorted(counts.items(), key=lambda x: x[1])
#lst1 = list(counts.keys())
#lst.sort()
#lst1.sort()
#print(lst)
#print(lst1)
for key in lst:
   print(key[1], key[0])


#plt.plot(lst1, lst, "-r")

#plt.xlabel("xlabel")
#plt.ylabel("ylabel")

#plt.grid(alpha=0.4)

#plt.title("distribuzione parole")

#plt.show()
