from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.tuotteet = {}

    def tavaroita_korissa(self):
        pass
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        maara = 0
        for tuote in self.tuotteet.values():
            maara += tuote.lukumaara()
        return maara 

    def hinta(self):
        hinta = 0
        for tuote in self.tuotteet.values():
            hinta += tuote.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi in self.tuotteet:
            self.tuotteet[lisattava.nimi].muuta_lukumaaraa(1)
        else:
            self.tuotteet[lisattava.nimi] = Ostos(lisattava)
        pass

    def poista_tuote(self, poistettava: Tuote):
        if not poistettava.nimi in self.tuotteet:
            return
        if self.tuotteet[poistettava.nimi].lukumaara() == 0:
            self.tuotteet.pop(poistettava.nimi)
        else:
           self.tuotteet[poistettava.nimi].muuta_lukumaaraa(-1) 
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        ostokset = []
        for tuote in self.tuotteet.values():
            ostokset.append(tuote)
        return ostokset
