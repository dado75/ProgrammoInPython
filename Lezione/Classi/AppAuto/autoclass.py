class Mezzi_trasporto:

    def __init__(self, tipologia, sost_amb, pubblico):
        self.tipologia = tipologia
        self.sost_amb = sost_amb
        self.pubblico = pubblico

    def scheda_mezzo_trasporto(self):
        scheda = f"""
        Tipologia mezzo trasporto: {self.tipologia}
        Sostenibilità ambientale: {self.sost_amb}
        Pubblico/Privato: {self.pubblico}"""
        return scheda

    @classmethod
    def from_string(cls, stringa_mezzo):
        tipologia, sost_amb, pubblico = stringa_mezzo.split("-")
        return cls(tipologia, sost_amb, pubblico)

    def modifica_scheda_mezzo_trasporto(self):
        print(""" Modifica Scheda:
        1 = Tipologia mezzo trasporto
        2 = Sostenibilità ambientale
        3 = Pbblico/Privato """)
        scegli = input("Cosa desideri modificare?")
        if scegli == "1":
            self.tipologia = input("Nuova Tipologia -->")
        if scegli == "2":
            self.sost_amb = input("Valore sost. ambientale -->")
        if scegli == "3":
            self.pubblico = input("Pubblico/Privato -->")


    def voto_sost_ambientale(self, valutazione):
        self.sost_amb += valutazione

class Automobile(Mezzi_trasporto):

    profilo = "Automobile"

    def __init__(self, tipologia, sost_amb, pubblico, marca, chilometri, colore, serbatoio, optional=None):
        super().__init__(tipologia, sost_amb, pubblico)
        self.marca = marca
        self.chilometri = chilometri
        self.colore = colore
        self.serbatoio = serbatoio
        if optional is None:
            self.optional = []
        else:
            self.optional = optional

    def scheda_auto(self):
        scheda = f"""
        Profilo:  {Automobile.profilo}
        Marca: {self.marca}
        Colore carrozzeria: {self.colore}
        Elenco Optional : {self.optional}
        Benzina nel serbatoio: {self.serbatoio}
        Chilometri percorsi: {self.chilometri} """
        return super().scheda_mezzo_trasporto() + scheda

    def modifica_scheda_auto(self):
        print(""" Modifica Scheda:
        1 = Marca
        2 = Colore carrozzeria
        3 = Elenco Optional
        4 = Benzina nel serbatoio
        5 = Chilometri percosi """)
        scegli = input("Cosa desideri modificare?")
        if scegli == "1":
            self.marca = input("Inserisci la marca -->")
        if scegli == "2":
            self.colore = input("Nuovo colore -->")
        if scegli == "3":
            self.optional = input("Aggiungi optional -->")
        if scegli == "4":
            self.serbatoio = input("Nuovo livello serbatoio -->")
        if scegli == "5":
            self.chilometri = input("Aggiorna i km percorsi -->")

    def guida(self, chilometri):
        self.chilometri += chilometri

    def fai_il_pieno(self, litri):
        self.serbatoio += litri

auto = Automobile('elettrica', 8, 'privato', 'Tesla' , 0, 'nera', 50, [ 'aria condizionata', 'vetri oscurati'])
mezzo = Mezzi_trasporto('idrogeno', 10,'privato')
print(mezzo.scheda_mezzo_trasporto())

print('km iniziali: ', auto.chilometri)
auto.guida(1000)
print('km finali: ', auto.chilometri)

print('serbatoio iniziale: ', auto.serbatoio)
auto.fai_il_pieno(50)
print('serbatoio finale: ', auto.serbatoio)

print(auto.scheda_auto())

#print(help(Automobile))

auto.modifica_scheda_auto()
print(auto.scheda_auto())

monopattino_elettrico = "elettrica-10-privato"
mezzo_trasporto1 = Mezzi_trasporto.from_string(monopattino_elettrico)

print(mezzo_trasporto1.scheda_mezzo_trasporto())

print(auto.scheda_mezzo_trasporto())