import unittest
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path

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

    def test_setFelder(self):
        """
        Überprüft, ob Spielsteine korrekt gesetzt werden.
        ________________________________________________

        assertEqual() ist eine Unittest library Funktion, welche die gleichwertigkeit von 2 Werten überprüft.
        Wenn beide Werte gleichwertig sind, gibt assertEqual() True zurück, andernfalls False.
        """
        self.Feld1.setFelder(0)
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

    def test_Spielzug(self):
        """
        Überprüft, ob ein Zug möglich ist.
        _________________________________

        assertTrue() ist eine weitere Unittest library Funktion, welche den test Wert mit True vergleicht.
        Diese Funktion wird je nach Bedingung einen boolean zurückliefern. Falls der test Wert True ist,
        dann gibt assertTrue() den Wert True zurück, andernfalls False.
        """

    def test_gueltige_spalte(self):
        """
        Überprüft die Funktion setFelder.
        """
        for i in range(6):
            self.Feld1.setFelder(1)
        print(self.Feld1.setFelder(1))

if __name__ == '__main__':
    unittest.main()
