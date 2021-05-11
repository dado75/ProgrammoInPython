#def stampo_queste_righe():
#    print('stiamo studiando le funzioni')
#    print('Che bello!!!')

#stampo_queste_righe()

#da_invertire = "davide"

#def inverti_stringa(stringa):
#    indice = (len(stringa) -1)
#    nuova_stringa = ""
#    while indice >= 0:
#        nuova_stringa += stringa[indice]
#        indice -= 1
#    print(nuova_stringa)

#inverti_stringa(da_invertire)

word = 'in mezzo al cammin di nostra vita'
d = dict()

for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
    d[c] = d.get(c,0) + 1
print(d)

#counts = {'Marco': 4, 'Simone': 89, 'Antonio': 8, 'Luigi': 78}
#for key in counts:
#    if counts[key] > 5:
#        print(key, counts[key])

#counts = {'Marco': 4, 'Simone': 89, 'Antonio': 8, 'Luigi': 78}
#lst = list(counts.keys())
#print(lst)
#lst.sort()
#for key in lst:
#   print(key, counts[key])