import string

# apro il file di testo
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File connot be opened:' , fname)
    exit()

counts = dict()

#elimino i caratteri a capo (chr10 chr13)
fhand = fhand.rstrip()
#elimino la punteggiatura
fhand = fhand.translate(fhand.maketrans('', '', string.punctuation))
#porto tutto minuscolo
fhand = fhand.lower()
#separo le parole e creo una lista di parole
words = fhand.split()
for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
#        counts[word] = counts.get(word,0) + 1

print(counts)

#lst = list(counts.keys())
#print(lst)
#lst.sort()
for key in counts:
   print(key, counts[key])