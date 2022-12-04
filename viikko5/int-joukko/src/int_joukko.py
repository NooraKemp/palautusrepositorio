class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.lukujono = []

    def kuuluu(self, n):
        if n in self.lukujono:
            return True
        return False

    def lisaa(self, n):
        if n not in self.lukujono:
           self.lukujono.append(n)

    def poista(self, n):
        if n in self.lukujono:
            self.lukujono.remove(n)

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return self.lukujono

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        taulu = a.to_int_list() + b.to_int_list()

        for i in taulu:
            yhdiste.lisaa(i)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        
        for a in a.to_int_list():
            if a in b.to_int_list():
               leikkaus.lisaa(a)
        
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()

        for a in a.to_int_list():
            if a not in b.to_int_list():
               erotus.lisaa(a)  

        return erotus

    def __str__(self):
        if len(self.lukujono) == 0:
            return "{}"
        if len(self.lukujono) == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0 ,len(self.lukujono) - 1):
                tuotos += str(self.lukujono[i]) + ", "
            tuotos += str(self.lukujono[len(self.lukujono) - 1]) + "}"
            return tuotos
