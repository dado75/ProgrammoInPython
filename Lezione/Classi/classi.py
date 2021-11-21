"""Classi modello generico che genera oggetti 
con le stesse proprietà chiamati istanze 
"""
class Studente:
    
    #variabili di classe
    ore_settimanali = 36
    corpo_studentesco = 0
    
    #metodo inizializzatore self attribuisce le variabili dette "variabili di istanza" a tutte le istanze 
    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        Studente.corpo_studentesco += 1

    #def __add__(self, other):
    #    """solo a fini didattici"""
    #    return self.nome + " " + other.corso_di_studi

    #def __str__(self):
    #    """rapresentazione leggibile per utente"""
     #   return f"Lo studente {self.nome} {self.cognome}"
        
    def __repr__(self):
        """rappresentaizone non ambigua per sviluppatore"""
        return f"Studente ( {self.nome}, {self.cognome}, {self.corso_di_studi} )"


    def scheda_personale(self):
        return f"Scheda Studente:\n Nome:{self.nome}\n Cognome:{self.cognome}\n Corso di Studi:{self.corso_di_studi}\n Ore Settimanali:{self.ore_settimanali}\n Corpo Studentesco:{Studente.corpo_studentesco}"

#istanze (oggetti generati e modellati secondo le caratteristiche della classe)
studente_uno = Studente("Giovanni", "Migliorini", "Statistica")
studente_due = Studente("Marina", "Siniscalchi", "Matematica")
studente_tre = Studente("Paolo", "Baldini", "Informatica")
#print(Studente.corpo_studentesco)

#studente_uno.ore_settimanali += 4
print(studente_uno.scheda_personale())
print(studente_due.scheda_personale())

print(Studente.scheda_personale(studente_tre))
#print(studente_uno + studente_due)

print(studente_uno.__str__())
print(studente_tre.__repr__())
print(Studente.__repr__(studente_tre))


