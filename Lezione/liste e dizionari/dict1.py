import string

# apro il file di testo
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File connot be opened:' , fname)
    exit()

counts = dict()
for line in fhand:
    #elimino i caratteri a capo
    line = line.rstrip()
    #elimino la punteggiatura
    line = line.translate(line.maketrans('', '', string.punctuation))
    #porto tutto minuscolo
    line = line.lower()
    #separo le parole
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
#
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
   print(key, counts[key])