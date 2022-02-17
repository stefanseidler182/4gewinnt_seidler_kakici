import unittest
import sys
import os
import io
from pathlib import Path
myDir = os.getcwd()
sys.path.append(myDir)
path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)
from viergewinnt.main import *


class ViergewinntTests(unittest.TestCase):
    def setUp(self):
        self.Spieler1 = Spielmodus(1)
        self.Spieler2 = Spielmodus(2)
        self.Feld1 = Spielfeld()
        self.gui1 = GUI()
        self.spielregeln1 = Spielregeln()

    def test_Spielmodus(self):
        """
        Überprüft, ob andere Spielmodi als 1 und 2 möglich sind.
        """
        self.assertRaises(ValueError, Spielmodus, 3)
        self.assertRaises(ValueError, Spielmodus, "H")

    def test_Spielfeld(self):
        """
        Überprüft, ob Spielsteine korrekt gesetzt werden.
        ________________________________________________

        assertEqual() ist eine Unittest library Funktion, welche die gleichwertigkeit von 2 Werten überprüft.
        Wenn beide Werte gleichwertig sind, gibt assertEqual() True zurück, andernfalls False.
        """
        print(ZAEHLER)
        self.Feld1.setFelder(0)
        self.gui1.printSpielfeld(self.Feld1)
        erg1 = self.Feld1.getFelder()
        self.assertEqual(erg1, [[".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        self.Feld1.setFelder(0)
        erg2 = self.Feld1.getFelder()
        self.assertEqual(erg2, [[".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        self.Feld1.setFelder(0)
        self.Feld1.setFelder(0)
        self.Feld1.setFelder(0)
        erg3 = self.Feld1.getFelder()
        self.assertEqual(erg3, [[".", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        self.Feld1.setFelder(0)
        erg4 = self.Feld1.getFelder()
        self.assertEqual(erg4, [["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        reihe = self.Feld1.getLetzteReihe()
        spalte = self.Feld1.getLetzteSpalte()
        self.assertEqual(spalte, 0)
        self.assertEqual(reihe, 0)

    def test_gueltige_Spalte(self):
        self.assertRaises(IndexError, self.Feld1.setFelder, 8)

    def test_Spielzug(self):
        """
        Überprüft, ob ein Zug möglich ist.
        _________________________________

        assertTrue() ist eine weitere Unittest library Funktion, welche den test Wert mit True vergleicht.
        Diese Funktion wird je nach Bedingung einen boolean zurückliefern. Falls der test Wert True ist,
        dann gibt assertTrue() den Wert True zurück, andernfalls False.
        """

    def test_gewonnen(self):
        """
        Überprüft die Funktion gewonnen. Spieler 1 wirft immer in Spalte 1 und Spieler 2 wirft immer in Spalte 2.
        """
        for i in range(7):
            self.Feld1.setFelder(1)
            self.Feld1.setFelder(2)
        self.assertEqual(self.spielregeln1.gewonnen(self.Feld1), True)
        for i in range(6):
            self.Feld1.setFelder(1)
            self.Feld1.setFelder(2)
        self.assertEqual(self.spielregeln1.gewonnen(self.Feld1), True)


    def test_printSpielfeld(self):
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.gui1.printSpielfeld(self.Feld1)
        sys.stdout = sys.__stdout__
        self.assertEqual('. . . . . . .\n'
                          '. . . . . . .\n'
                          '. . . . . . .\n'
                          '. . . . . . .\n'
                          '. . . . . . .\n'
                          '. . . . . . .\n'
                          , capturedoutput.getvalue())


if __name__ == '__main__':
    unittest.main()
