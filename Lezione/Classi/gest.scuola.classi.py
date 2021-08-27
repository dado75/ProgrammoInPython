class Persona:

    istituto = "Scuola Superiore"

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    @classmethod    
    def from_string(cls, stringa_persona, *args):
        nome, cognome, età, residenza = stringa_persona.split("-")
        return cls(nome, cognome, età, residenza, *args)

    @classmethod
    def occupazione(cls):
        if cls.__name__ == "Studente":
            return "Studente"
        else:
            return "Insegnante"

    @staticmethod
    def info_prog():
        info = """
        Nome: Persona
        Creato da: Davide Piccolo
        Commenti: Primo programma serio in python 3.7"""

        return info
        
        
    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome} 
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")
        scelta = input("Cosa Desideri modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome--> ")
        elif scelta == "2":
            self. cognome = input("Nuovo Cognome --> ")
        elif scelta == "3":
            self.età = int(input("Nuova età --> "))
        elif scelta == "4":
            self.residenza = input("Nuova Residenza --> ")


class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso di studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda

    def cambio_corso(self, corso):
        self.corso_di_studio = corso
        print("Corso Aggiornato")

        
class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self, nome, cognome, età, residenza, materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Insegnante.profilo}
        Materie insegnate:{self.materie}
        ***"""
        return super().scheda_personale() + scheda

    def aggiungi_materia(self, nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco materie aggiornato")

    def __str__(self):
        return f"Profilo"

    def __repr__(self):
        pass

        
studente_uno = Studente("Marco", "Albera", 24, "Vicenza", "Sociologia")
studente_due = Studente("Luigi", "Einaudi", 27, "Milano", "Sociologia")
insegnante_uno = Insegnante("Simone", "Allegri", 54, "Torino", ["Sociologia delle religioni", "Sociologia generale"])
print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale())

insegnante_uno.aggiungi_materia("Sociologia della comunicazione")
studente_uno.cambio_corso("Filosofia")
print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale())
print(help(Studente))

Ginetto = "Gino-Peppino-40-Sorrento"
semetto = "Orlando-Cazzone-56-Cesenatico"

insg1 = Insegnante.from_string(Ginetto, "Tuttologia")
stud1 = Studente.from_string(semetto, "Deficentologia")

print(insg1.occupazione())
print(stud1.occupazione())

print(Persona.info_prog())

Persona.modifica_scheda(studente_uno)
print(studente_uno.scheda_personale())

