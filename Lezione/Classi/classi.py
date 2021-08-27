class Studente:

    ore_settimanali = 36
    corpo_studentesco = 0
    
    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        Studente.corpo_studentesco += 1

        
    def scheda_personale(self):
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di Studi:{self.corso_di_studi}\n Ore Settimanali:{self.ore_settimanali}"


studente_uno = Studente("Giovanni", "Migliorini", "Statistica")
studente_due = Studente("Marina", "Siniscalchi", "Matematica")
print(Studente.corpo_studentesco)

studente_uno.ore_settimanali += 4
# print(studente_uno.scheda_personale())
# print(studente_due.scheda_personale())

# print(Studente.scheda_personale(studente_uno))

# print(Studente.__dict__)
# print(studente_uno.__dict__)
