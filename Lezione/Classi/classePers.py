#ereditarietà classe genitore/figlia
class Persona:
    istituto =""

    #i Metodi Statici sono funzioni che teniamo all'interno della classe 
    # perché hanno una qualche correlazione con il contesto che stiamo modellando, 
    # ma non vi sono legati direttamente, come accade invece nel caso della scheda personale 
    # o del costruttore alternativo.
    @staticmethod
    def info_prog():
        info = """
        Nome: Davide
        Creato da: Cairoli
        Commenti: Scritto usando Python 3"""

        return info
    
    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza
    
    def scheda_personale(self):
        scheda = f"""
        Istituto: {Persona.istituto}
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n
        """
        return scheda
    
    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza
        """)
        scegli = input("Cosa desideri modificare?")
        if scegli == "1":
            self.nome = input("Nuovo Nome --> ")
        elif scegli == "2":
            self.cognome = input("Nuovo Cognome --> ")
        elif scegli == "3":
            self.età = int(input("Nuova età -->"))
        elif  scegli == "3":
            self.residenza = input("Nuova Residenza --> ")

    #metodo costruttore alternativo con decoratore 
    #(di classe cioè ci permette di passare la classe invece del metodo)
    @classmethod
    def from_string(cls, stringa_persona, *args):
        nome, cognome, età, residenza = stringa_persona.split(";")
        return cls(nome, cognome, età, residenza, *args)

    #i Metodi di Classe si dimostrano utili, 
    #qualora vogliate un Metodo che cambia comporamento in base alla sottoclasse 
    #che lo sta richiamando. Ad esempio, possiamo creare un Metodo chiamato occupazione, 
    #che ci permette di identificare uno studente o un insegnante
    #senza dover passare per la scheda personale.
    @classmethod
    def occupazione(cls):
        return cls.__name__
        #if (cls.__name__ == "Studente"):
        #    return "Studente"
        #else:
        #    return "Insegnante"

    @classmethod
    def cambia_istituto(cls):
        Persona.istituto = input("Nuovo Istituto --> ")
        return Persona.istituto
        
            
#classe figlia eredita tutte le proprietà della classe genitore
class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studi):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studi = corso_di_studi
    
    def scheda_personale(self):
        scheda = f"""
        Profilo: {Studente.profilo}
        Corso di studi: {self.corso_di_studi}
        """
        return super().scheda_personale() + scheda

#altra classe figlia che ci permette di definire proprietà diverse attraverso metodi diversi
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
        ***
        """
        return super().scheda_personale() + scheda

    def aggiungi_materia(self,nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco materie Aggiornato")
    

class Collaboratore(Persona):
    pass

class Personale_amministrativo(Persona):
    pass

prima_persona = Studente("Marco", "Rossi", "14", "Torino", "Secondaria")
seconda_persona = Studente("Simone", "Grandi", "15", "Asti", "Secondaria")
terza_persona = Insegnante("Antonio", "Russo", "45", "Alessandria")
quarta_persona = Collaboratore("Giovanni", "Riccio", "32", "Torino")
super_persona = "Marina; Sermonti; 40; Milano"
plus_persona = "Giovanni; Lopolito; 45; Verona"

print(prima_persona.scheda_personale())
print(seconda_persona.scheda_personale())
#print(quarta_persona.scheda_personale())
print(terza_persona.scheda_personale())
terza_persona.aggiungi_materia("Matematica")
print(terza_persona.scheda_personale())
#print(terza_persona.modifica_scheda())
#print(terza_persona.scheda_personale())
#print(help(Insegnante))
quinta_persona = Persona.from_string(super_persona)
print(quinta_persona.scheda_personale())
ins_uno = Insegnante.from_string(plus_persona, ["Statistica", "Arte"])
print(ins_uno.scheda_personale())
ins_uno.aggiungi_materia("Informatica")
print(ins_uno.scheda_personale())
print(ins_uno.occupazione())
print(prima_persona.occupazione())
print(prima_persona.scheda_personale())
print(Persona.cambia_istituto())
print(Persona.istituto)
print(prima_persona.scheda_personale())
print(Persona.info_prog())