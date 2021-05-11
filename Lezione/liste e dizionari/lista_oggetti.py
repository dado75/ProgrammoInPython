def lista_oggetti():
    oggetti = []
    oggetto = ""
    while True:
        oggetto = input('Che oggetto vuoi aggingere alla lista? ')
        if oggetto == "CARCIOFO":
            print('Carciofo!! Stai uscendo...')
            break
        else:
            oggetti.append(oggetto)

    print('Gli oggetti della lista sono: ' + str(oggetti))

lista_oggetti()