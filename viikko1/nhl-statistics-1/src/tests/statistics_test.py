import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_palauttaa_none_jos_pelaaja_ei_ole_listalla(self):
        self.assertEqual(self.statistics.search("Koivu"), None)

    def test_palauttaa_pelaajan(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")

    def test_palauttaa_listan(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)

    def test_palauttaa_topPisteet_oikein(self):
        self.assertEqual(self.statistics.top(3, 1)[0].name, "Gretzky")

    def test_palauttaa_topMaalit_oikein(self):
        self.assertEqual(self.statistics.top(3, 2)[0].name, "Lemieux") 

    def test_palauttaa_topSyoto_oikein(self):
        self.assertEqual(self.statistics.top(3, 3)[0].name, "Gretzky")  
    

        

