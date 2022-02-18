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
ZAEHLER = 0



class ViergewinntTests(unittest.TestCase):
    def setUp(self):
        self.Spieler1 = Spielmodus(1)
        self.Spieler2 = Spielmodus(2)
        self.spielfeld = Spielfeld()
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

        assertEqual() ist eine Unittest library Funktion, welche die Gleichwertigkeit von 2 Werten überprüft.
        Wenn beide Werte gleichwertig sind, gibt assertEqual() True zurück, andernfalls False.
        """
        self.spielfeld.setFelder(0)
        erg1 = self.spielfeld.getFelder()
        self.assertEqual(erg1, [[".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        self.spielfeld.setFelder(0)
        erg2 = self.spielfeld.getFelder()
        self.assertEqual(erg2, [[".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        self.spielfeld.setFelder(0)
        self.spielfeld.setFelder(0)
        self.spielfeld.setFelder(0)
        erg3 = self.spielfeld.getFelder()
        self.assertEqual(erg3, [[".", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        self.spielfeld.setFelder(0)
        erg4 = self.spielfeld.getFelder()
        self.assertEqual(erg4, [["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."],
                                ["0", ".", ".", ".", ".", ".", "."],
                                ["X", ".", ".", ".", ".", ".", "."]])
        reihe = self.spielfeld.getLetzteReihe()
        spalte = self.spielfeld.getLetzteSpalte()
        self.assertEqual(spalte, 0)
        self.assertEqual(reihe, 0)

    def test_gueltige_Spalte(self):
        self.assertRaises(IndexError, self.spielfeld.setFelder, 8)
        '''
        Überprüft ob ein IndexError angezeigt wird, wenn der Spieler eine Spalte
        außerhalb einer range von 1-7 auswählt
        '''


    def test_gewonnen_vertikal(self):
        """
        Überprüft die Funktion gewonnen. Spieler 1 wirft immer in Spalte 1 und Spieler 2 wirft immer in Spalte 2.
        """
        self.spielfeld.setFelder(1)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(1)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(1)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(1)
        self.assertEqual(self.spielregeln1.gewonnen(self.spielfeld), True)

    def test_gewonnen_horizontal(self):

        self.spielfeld.setFelder(1)
        self.spielfeld.setFelder(1)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(3)
        self.spielfeld.setFelder(3)
        self.spielfeld.setFelder(4)
        self.assertEqual(self.spielregeln1.gewonnen(self.spielfeld), True)

    def test_gewonnen_diagonal_links_oben(self):
        self.spielfeld.setFelder(4)
        self.spielfeld.setFelder(4)
        self.spielfeld.setFelder(3)
        self.spielfeld.setFelder(5)
        self.spielfeld.setFelder(5)
        self.spielfeld.setFelder(3)
        self.spielfeld.setFelder(5)
        self.spielfeld.setFelder(3)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(2)
        self.spielfeld.setFelder(2)
        self.assertEqual(self.spielregeln1.gewonnen(self.spielfeld), True)

    def test_gewonnen_diagonal_rechts_oben(self):
        self.spielfeld.setFelder(4)
        self.spielfeld.setFelder(4)
        self.spielfeld.setFelder(5)
        self.spielfeld.setFelder(3)
        self.spielfeld.setFelder(5)
        self.spielfeld.setFelder(5)
        self.spielfeld.setFelder(6)
        self.spielfeld.setFelder(6)
        self.spielfeld.setFelder(6)
        self.spielfeld.setFelder(6)
        self.assertEqual(self.spielregeln1.gewonnen(self.spielfeld), True)

    def test_printSpielfeld(self):
        capturedoutput = io.StringIO()
        sys.stdout = capturedoutput
        self.gui1.printSpielfeld(self.spielfeld)
        sys.stdout = sys.__stdout__
        self.assertEqual('. . . . . . .\n'
                         '. . . . . . .\n'
                         '. . . . . . .\n'
                         '. . . . . . .\n'
                         '. . . . . . .\n'
                         '. . . . . . .\n', capturedoutput.getvalue())

    def test_voll(self):
        """
        Überprüft, ob das Spielfeld voll ist.
        """
        self.assertFalse(self.spielregeln1.voll(self.spielfeld))
        for _ in self.spielfeld.getFelder():
            for i in range(0, 7):
                self.spielfeld.setFelder(i)
        # self.gui1.printSpielfeld(self.spielfeld)
        self.assertTrue(self.spielregeln1.voll(self.spielfeld))

    def test_spielstart(self):
        """
        Die Funktion simuliert das Spiel von 2 Computerspielern, ohne das Spielfeld auszugeben.
        Je öfter man es simuliert, desto mehr Fehler können gefunden werden.
        """
        spielmodus_spieler1 = 2
        self.Spieler1.spielmodus = spielmodus_spieler1
        spielmodus_spieler2 = 2
        self.Spieler2.spielmodus = spielmodus_spieler2
        #self.gui1.printSpielfeld(self.spielfeld)
        while True:
            ueberpruefe_spielzug_spieler1 = False
            spielzug_spieler_1 = None
            if spielmodus_spieler1 == 1:
                beenden = self.gui1.beenden()
                if beenden:
                    print("Spieler 2 hat gewonnen!")
                    break
            while not ueberpruefe_spielzug_spieler1:
                spielzug_spieler_1 = self.Spieler1.spielzug(self.gui1)
                ueberpruefe_spielzug_spieler1 = self.spielregeln1.volleSpalte(self.spielfeld, spielzug_spieler_1)

            self.spielfeld.setFelder(spielzug_spieler_1)
            #self.gui1.printSpielfeld(self.spielfeld)
            if self.spielregeln1.voll(self.spielfeld):
                print("Das Spielfeld ist voll. UNENTSCHIEDEN!")
                break
            if self.spielregeln1.gewonnen(self.spielfeld):
                #print("Spieler 1 hat gewonnen!")
                break

            ueberpruefe_spielzug_spieler2 = False
            spielzug_spieler_2 = None
            if spielmodus_spieler2 == 1:
                beenden = self.gui1.beenden()
                if beenden:
                    print("Spieler 1 hat gewonnen!")
                    break
            while not ueberpruefe_spielzug_spieler2:
                spielzug_spieler_2 = self.Spieler2.spielzug(self.gui1)
                ueberpruefe_spielzug_spieler2 = self.spielregeln1.volleSpalte(self.spielfeld, spielzug_spieler_2)

            self.spielfeld.setFelder(spielzug_spieler_2)
            #self.gui1.printSpielfeld(self.spielfeld)
            if self.spielregeln1.voll(self.spielfeld):
                print("Das Spielfeld ist voll. UNENTSCHIEDEN!")
                break
            if self.spielregeln1.gewonnen(self.spielfeld):
                #print("Spieler 2 hat gewonnen!")
                break


if __name__ == '__main__':
    unittest.main()
