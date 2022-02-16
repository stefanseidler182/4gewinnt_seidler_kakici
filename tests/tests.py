import unittest
from viergewinnt.main import Spielfeld, GUI, Spielregeln, Spielmodus, DasSpiel
'''
Hey Stefan! Hab game.main in viergewinnt geändert weil es das Modul game nicht findet.
Aber das Modul viergewinnt findet es auch nicht.
'''

class ViergewinntTests(unittest.TestCase):
    def __init__(self):
        self.spielmodus = None

    def spielmodus(self):
        self.spielmodus = Spielmodus(1)  # add assertion here

    def test_setFelder(self):
        """
        Überprüft, ob Spielsteine korrekt gesetzt werden.
        ________________________________________________

        assertEqual() ist eine Unittest library Funktion, welche die gleichwertigkeit von 2 Werten überprüft.
        Wenn beide Werte gleichwertig sind, gibt assertEqual() True zurück, andernfalls False.
        """
        self.Feld1.setFelder(0, "X")
        erg1 = self.Feld1.getFelder()
        self.assertEqual(erg1, [[" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])
        self.Feld1.setFelder(0, "X")
        erg2 = self.Feld1.getFelder()
        self.assertEqual(erg2, [[" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                [" ", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])
        self.Feld1.setFelder(0, "O")
        self.Feld1.setFelder(0, "O")
        self.Feld1.setFelder(0, "O")
        erg3 = self.Feld1.getFelder()
        self.assertEqual(erg3, [[" ", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])
        self.Feld1.setFelder(0, "O")
        erg4 = self.Feld1.getFelder()
        self.assertEqual(erg4, [["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["O", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "],
                                ["X", " ", " ", " ", " ", " ", " "]])


def test_Spielzug(self):
    """
    Überprüft, ob ein Zug möglich ist.
    _________________________________

    assertTrue() ist eine weitere Unittest library Funktion, welche den test Wert mit True vergleicht.
    Diese Funktion wird je nach Bedingung einen boolean zurückliefern. Falls der test Wert True ist,
    dann gibt assertTrue() den Wert True zurück, andernfalls False.
    """
    self.Feld1.setFelder(1, "X")
    # self.gui1.printSpielfeld(self.Feld1)
    self.assertTrue(self.spielregeln1.Spielzug(self.Feld1, 1))
    self.Feld1.setFelder(1, "X")
    self.assertTrue(self.spielregeln1.Spielzug(self.Feld1, 1))
    self.Feld1.setFelder(1, "X")
    self.assertTrue(self.spielregeln1.Spielzugy(self.Feld1, 1))
    self.Feld1.setFelder(1, "X")
    self.assertTrue(self.spielregeln1.Spielzug(self.Feld1, 1))
    self.Feld1.setFelder(1, "X")
    self.assertTrue(self.spielregeln1.Spielzug(self.Feld1, 1))
    self.Feld1.setFelder(1, "X")
    # self.gui1.printSpielfeld(self.Feld1)


if __name__ == '__main__':
    unittest.main()
