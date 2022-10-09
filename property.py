class Kunde:
    def __init__(self, vorname, nachname, guthaben=0):
        self.nachname = nachname
        self.vorname = vorname
        self._guthaben = guthaben
    @property
    def guthaben(self):
        return self._guthaben

    @guthaben.setter
    def guthaben(self, amount):
        if type(amount) != int:
            raise AttributeError("Attribut kann nur int sein.")
        self._guthaben = amount

    @guthaben.deleter
    def guthaben(self):
        del self._guthaben
        
    def einzahlen(self, amount):
        self._guthaben = self._guthaben + amount

        
kunde1 = Kunde("Max", "Mustermann", guthaben = 200)

print(kunde1.guthaben)


