class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def kumoa():
        pass

class Summa:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus
    
    def suorita(self):
        self.edellinen_tulos = self.sovellus.tulos
        self.sovellus.tulos += int(self.io())
        self.sovellus.kumoa = self.kumoa
    
    def kumoa(self):
        self.sovellus.tulos = self.edellinen_tulos


class Erotus:
    def __init__(self, sovellus, io):
        self.io = io
        self.sovellus = sovellus
    
    def suorita(self):
        self.edellinen_tulos = self.sovellus.tulos
        self.sovellus.tulos -= int(self.io())
        self.sovellus.kumoa = self.kumoa
    
    def kumoa(self):
        self.sovellus.tulos = self.edellinen_tulos


class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus
    
    def suorita(self):
        self.edellinen_tulos = self.sovellus.tulos
        self.sovellus.tulos = 0
        self.sovellus.kumoa = self.kumoa
    
    def kumoa(self):
        self.sovellus.tulos = self.edellinen_tulos


class Kumoa:
    def __init__(self, sovellus):
        self.sovellus = sovellus
    
    def suorita(self):
        self.sovellus.kumoa()