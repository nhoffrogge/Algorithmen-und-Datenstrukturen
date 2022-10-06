class Kunde:
    def __init__(self, vorname, nachname, guthaben=0):
        self.nachname = nachname
        self.vorname = vorname
        self.guthaben = guthaben
        
    def einzahlen(self, amount):
        self.guthaben = self.guthaben + amount
        
kunde1 = Kunde("Max", "Mustermann", guthaben = 200)

kunde1.guthaben = "hi"

kunde1.einzahlen(200)



