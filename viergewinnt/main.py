
from typing import List
from random import randint


class Spielfeld:
    """
    Die Klasse Spielfeld umfasst alle Informationen bezüglich des Spielfeldes.
    Das Spielfeld selbst ist ein Array aus 6 Listen bestehend aus 7 strings(Punkten).
    """

    def __init__(self):
        self.__felder = [[".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", "."]]
        self.__letzteSpalte = None
        self.__letzteReihe = None
        self.zaehler = 0

    def getFelder(self) -> List:
        """
        übermittelt das Spielfeld

        Returns
        -------
        List [List] - self.__felder
        """
        return self.__felder

    def setFelder(self, spalte: int):
        """
        Setzt Spielstein in die jeweilige Spalte.
        Ziel der Funktion ist es, dass der gespielte Stein bis zum
        letztmöglichen Punkt fällt, und nicht z.B. in der ersten Zeile hängen bleibt.
        ________________________________________
        Parameter:
        ----------------------------------------
        spalte: int
            Gibt die Spalte an, die vom Spieler ausgewählt wurde, um den Stein zu setzen
        """
        self.__letzteSpalte = spalte
        geworfen = False
        reihe = 5
        for liste in reversed(self.__felder):
            if not geworfen:
                if liste[spalte] == ".":
                    if (self.zaehler % 2) == 0:
                        liste[spalte] = 'X'
                        self.zaehler += 1
                    else:
                        liste[spalte] = '0'
                        self.zaehler += 1
                    self.__letzteReihe = reihe
                    geworfen = True
                elif liste[spalte] != ".":
                    reihe -= 1
                    self.__letzteReihe = reihe

    def getLetzteReihe(self) -> int:
        """
        Gibt jene Reihe an, die zuletzt im Spiel bespielt wurde.
        Die Zählung fängt bei 0 von der obersten Reihe an

        Returns
        -------
        int: self.__letzteReihe
        """
        return self.__letzteReihe

    def getLetzteSpalte(self) -> int:
        """
        Gibt jene Spalte an, die zuletzt im Spiel bespielt wurde.
        Die Zählung fängt bei 0 von links an

        Returns
        -------
        int: self.__letzteSpalte
        """
        return self.__letzteSpalte


class GUI:
    """
    Die Klasse GUI umfasst alle Informationen bezüglich des
    Graphical User Interfaces.
    """

    def __init__(self):
        self.spieler = 0  # Die Variable Spieler dient dazu, die Spieler, Spieler 1 und 2 zu benennen.

    def printSpielfeld(self, feld: Spielfeld):
        """
        Gibt das Spielfeld aus.
        ________________________________________
        Parameter:
        ----------------------------------------
        feld: Spielfeld
            Übergibt das aktuelle Spielfeld.
        """
        for liste in feld.getFelder():
            print(liste[0], liste[1], liste[2], liste[3], liste[4], liste[5], liste[6])

    def getSpielmodus(self) -> int:
        """
        Die Funktion fordert vom Spieler eine Eingabe.
        Je nach Eingabe wird ein von zwei Spielmodi ausgewählt.
        Die Aufforderung wird so lange wiederholt, bis die Eingabe valide ist. (Parameter 1 oder 2)
        ________________________________________
        Returns:
        ----------------------------------------
        int:
            Gibt den Spielmodus des jeweiligen Spielers zurück.
        """
        gueltigeModi = [1, 2]
        spielmodus = 0
        self.spieler += 1
        while spielmodus not in gueltigeModi:
            try:
                spielmodus = int(input(f'Spieler {self.spieler}: Bist du ein Mensch(1) oder ein Computer(2)'))
                if spielmodus not in gueltigeModi:
                    print(f'FALSCHE EINGABE! Bist du ein Mensch(1) oder ein Computer(2)')
                    continue
            except ValueError:
                print(f'FALSCHE EINGABE! Bist du ein Mensch(1) oder ein Computer(2)')
        return spielmodus

    def beenden(self) -> bool:
        """
        Die Funktion dient zum frühzeitigen Abbruch des Spiels und ermöglicht dem Spieler somit
        das Spiel jederzeit beenden zu können. while i < 1 mit i = 0 ist eine Endlosschleife, somit wird nach jedem
        Zug ein input benötigt (j oder n). Durch diesen input bricht man aus der Schleife raus. Die
        else Bedingung trifft nur im Falle einer ungültigen Eingabe des Spielers zu.
        Returns:
        ----------------------------------------
        bool:
            Gibt True für Beenden und False für Weiterspielen zurück.
        """
        i = 0
        while i < 1:
            beenden = input(f'Möchtest du das Spiel beenden?(j/n)')
            if beenden == "j":
                return True
            elif beenden == "n":
                return False
            else:
                print(f'FALSCHE EINGABE! Gib "j"(beenden) oder "n"(weiterspielen) ein!')
                continue

    def erfasseSpielzug(self) -> int:
        """
        Die Funktion erfasst den eingegebenen Spielzug und überprüft dabei,
        ob es ein gültiger Spielzug ist. Falls der Spielzug nicht gültig ist,
        wird der Spieler zu einer erneuten Eingabe aufgefordert.
        Returns:
        ----------------------------------------
        int:
            Gibt den Spaltenwert - 1 zurück, da die Array-indizes von 0 bis 6 gehen und wir 1 bis 7 eingeben.
        """
        spalte = 0
        gueltige_spalten = [1, 2, 3, 4, 5, 6, 7]

        while spalte not in gueltige_spalten:
            try:
                spalte = int(input(f'In welche Spalte möchtest du werfen?'))
                if spalte not in gueltige_spalten:
                    print("FALSCHE EINGABE! Wähle eine Spalte von 1 - 7")
                else:
                    return spalte - 1
            except ValueError:
                print("FALSCHE EINGABE! Wähle eine Spalte von 1 - 7")


class Spielmodus:
    """
    Die Klasse Spielmodus umfasst alle Informationen bezüglich des Spielmodus
    """

    def __init__(self, spielmodus: int):
        """
        Die Funktion wählt abhängig von der Eingabe des Spielers den jeweiligen
        Spielmodus und überprüft gleichzeitig, ob die Eingabe gültig ist. Bei einer
        ungültigen Eingabe wird der Spieler zu einer erneuten Eingabe aufgefordert.
        """
        if spielmodus == 1 or spielmodus == 2:
            self.__spielmodus = spielmodus
        else:
            raise ValueError("Falsche Eingabe! Gib 1 ein, wenn du gegen einen Mensch spielen willst oder 2,"
                             "wenn du gegen einen Computergegner spielen willst.")

    @property
    def spielmodus(self):
        return self.__spielmodus

    @spielmodus.setter
    def spielmodus(self, value):
        self.__spielmodus = value

    def spielzug(self, gui: GUI) -> int:
        """
        Die Funktion Spielzug ruft für einen menschlichen Spieler, die Methode erfasse Spielzug auf.
        Für einen Computerspieler wird eine zufällige Spalte zwischen 0 und 6 ermittelt.
        Returns:
        ----------------------------------------
        int:
            Gibt den Spaltenwert, in den der Stein geworfen wird, zurück.
        """
        if self.__spielmodus == 1:
            spalte = gui.erfasseSpielzug()
            return spalte
        elif self.__spielmodus == 2:
            spalte = randint(0, 6)
            return spalte


class Spielregeln:
    """
    Die Klasse Spielregeln umfasst alle Informationen bezüglich den Regeln des Spiels
    """

    def __init__(self):
        self.richtungen = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

    def volleSpalte(self, feld: Spielfeld, spalte: int) -> bool:
        """
        Die Funktion überprüft, ob der jeweilige Spielzug des Spielers gültig ist.
        Falls die Spalte, in die der Spieler den Stein werden will, voll ist,
        wird der Spieler zu einer erneuten Eingabe aufgefordert.
        ----------------------------
        Parameter:
        ----------------------------
        feld:
            Das aktuelle Spielfeld wird übergeben.
        spalte:
            Die Spalte in die, der Stein geworfen wird, wird übergeben.
        ----------------------------
        Returns:
        ----------------------------
        bool:
            Gibt False zurück, wenn die Spalte voll ist, ansonsten True.
        """
        spielfeld = feld.getFelder()
        if spielfeld[0][spalte] != ".":
            print("Spielzug nicht möglich. Spalte voll.")
            return False
        else:
            return True

    def voll(self, feld: Spielfeld) -> bool:
        """
        Diese Funktion überprüft nach jedem Spielzug, ob das Spielfeld voll ist.
        Die Schleife überprüft vom Feld[0][0] (Feld links oben) bis zum Feld [0][5], ob
        ein Punkt auf dem Feld ist. Sobald dies der Fall ist, wird False returniert.

        Danach folgt eine eigene Abfrage für das Feld[0][6]. Sollte dies ein Punkt sein,
        wird False retourniert, ansonsten True.

        ----------------------------
        Parameter:
        ----------------------------
        feld:
            Das aktuelle Spielfeld wird übergeben.
        ----------------------------
        Returns:
        ----------------------------
        bool:
            Gibt False zurück, wenn das Spielfeld voll ist, ansonsten True.

        """
        spielfeld = feld.getFelder()
        for i in range(6):
            if spielfeld[0][i] == ".":
                return False
            else:
                continue
        if spielfeld[0][6] != ".":
            return True
        else:
            return False

    def gewonnen(self, feld: Spielfeld) -> bool:
        """
        Die Funktion überprüft ob einer der Spieler das Spiel gewonnen hat.
        Die Funktion ruft das Spielfeld sowie die Zeile und Spalte des zuletzt geworfenen Spielsteins ab.
        Die erste Schleife überprüft in alle 8 Richtungen. Zuerst wird, die Annahme getroffen, dass
        der Spieler gewonnen hat. Die zweite Schleife überprüft, für die jeweilige Richtung, ob 4 Steine in dieser
        Richtung im Spielfeld sind. Es wird jeweils eine neue Spalten- bzw. Zeilenposition ermittelt. Danach wird
        überprüft, ob die ermittelten Positionen sich im Spielfeld befinden. Falls das nicht der Fall ist,
        folgt ein break.
        Danach wird überprüft, ob schon 3 Steine in eine Richtung gefunden wurden.
        Sollte dies der Fall sein, werden neue Spalten- bzw. Zeilenpositionen ermittelt, die von der geworfenen
        Position in die Gegenrichtung zeigen. Dies dient dazu, falls der zuletzt geworfene Stein nicht am Ende
        vier in einer Richtung bildet, sondern auf einer mittleren Position eingeworfen wird. Sollte sich die
        ermittelte Position außerhalb des Spielfelds befinden, wird überprüft, ob in die andere Richtung gewonnen
        wurde.
        Sind noch keine 3 Steine in eine Richtung gefunden, wird überprüft, ob weitere Steine in die jeweilige
        Richtung vorhanden sind. Sobald alle Richtungen überprüft wurden, bricht die Schleife ab, und setzt
        den Wert von vier_in_einer_reihe auf False.
        Außerhalb der zweiten Schleife, wird am Ende überprüft, ob der Wert von vier_in_einer_reihe True ist.

        ----------------------------
        Parameter:
        ----------------------------
        feld:
            Das aktuelle Spielfeld wird übergeben.
        ----------------------------
        Returns:
        ----------------------------
        bool:
            Gibt False zurück, wenn das der nicht Spieler keine vier Steine in eine Richtung hat, ansonsten True.

        """
        spielfeld = feld.getFelder()
        zeile = feld.getLetzteReihe()
        spalte = feld.getLetzteSpalte()
        for i in range(8):
            vier_in_einer_reihe = True
            j = 1
            while j < 4:
                spaltenposition = spalte + self.richtungen[i][0] * j
                zeilenposition = zeile + self.richtungen[i][1] * j
                if zeilenposition > 5 or zeilenposition < 0 or spaltenposition > 6 or spaltenposition < 0:
                    j += 1
                    vier_in_einer_reihe = False
                    break
                if j == 3:
                    spaltenposition_2 = spalte + self.richtungen[i][0] * -1
                    zeilenposition_2 = zeile + self.richtungen[i][1] * -1
                    if zeilenposition_2 > 5 or zeilenposition_2 < 0 or spaltenposition_2 > 6 or spaltenposition_2 < 0:
                        if spielfeld[zeile][spalte] == spielfeld[zeilenposition][spaltenposition]:
                            j += 1
                            continue
                        else:
                            vier_in_einer_reihe = False
                            break
                    if spielfeld[zeile][spalte] == spielfeld[zeilenposition_2][spaltenposition_2]:
                        j += 1
                        continue
                if spielfeld[zeile][spalte] == spielfeld[zeilenposition][spaltenposition]:
                    j += 1
                    continue
                vier_in_einer_reihe = False
                break
            if vier_in_einer_reihe:
                return True


class DasSpiel:
    """
    Erstellt das Spiel.
    In der init Funktion wird das Spielfeld, das GUI, die Spielregeln sowie die Spielmodi
    initialisiert. Zuerst wird abgefragt, ob die Spieler Mensch oder Computer sind. In der spielStart-Funktion wird
    überprüft, ob das Spielfeld voll ist. Wenn das Spielfeld voll ist, wird Unentschieden ausgegeben. Nach jedem Zug
    wird ein menschlicher Spieler gefragt, ob er/sie aufgeben will(beenden). Nach jedem geworfenen Stein,
    wird überprüft, ob der Spieler gewonnen hat und das aktuelle Spielfeld wird ausgegeben.
    """

    def __init__(self):
        """
        Initialisiert das Spielfeld, die GUI, die Spielregeln sowie die Spielmodi der Spieler.
        """
        self.__feld = Spielfeld()
        self.__gui = GUI()
        self.__spielregeln = Spielregeln()
        self.spieler1 = Spielmodus(2)
        self.spieler2 = Spielmodus(2)

    def spielStart(self):
        """
        Zunächst werden die Spielmodi festgelegt (ob gegen Computer oder gegen Mensch).
        In der while True Schleife wird die beenden-Funktion nur dann ausgeführt, wenn der
        Spieler ein Mensch ist (Spielmodus 1). Wenn Spieler 1 das Spiel beendet, gewinnt
        Spieler 2. Danach wird der Spielzug abgefragt und überprüft. Der Spielzug ist dann gültig, wenn
        er nicht in eine Spalte geht, die voll ist. Danach wird der Spielzug durchgeführt und das Spielfeld
        ausgegeben. Anschließend wird überprüft, ob das Spielfeld voll ist und, ob der Spieler gewonnen hat.
        Dieselben Schritte werden beim Spieler 2 gemacht.
        """

        spielmodus_spieler1 = self.__gui.getSpielmodus()
        self.spieler1.spielmodus = spielmodus_spieler1
        spielmodus_spieler2 = self.__gui.getSpielmodus()
        self.spieler2.spielmodus = spielmodus_spieler2
        self.__gui.printSpielfeld(self.__feld)
        while True:
            ueberpruefe_spielzug_spieler1 = False
            spielzug_spieler_1 = None
            if spielmodus_spieler1 == 1:
                beenden = self.__gui.beenden()
                if beenden:
                    print("Spieler 2 hat gewonnen!")
                    break
            while not ueberpruefe_spielzug_spieler1:
                spielzug_spieler_1 = self.spieler1.spielzug(self.__gui)
                ueberpruefe_spielzug_spieler1 = self.__spielregeln.volleSpalte(self.__feld, spielzug_spieler_1)

            self.__feld.setFelder(spielzug_spieler_1)
            self.__gui.printSpielfeld(self.__feld)
            if self.__spielregeln.voll(self.__feld):
                print("Das Spielfeld ist voll. UNENTSCHIEDEN!")
                break
            if self.__spielregeln.gewonnen(self.__feld):
                print("Spieler 1 hat gewonnen!")
                break

            ueberpruefe_spielzug_spieler2 = False
            spielzug_spieler_2 = None
            if spielmodus_spieler2 == 1:
                beenden = self.__gui.beenden()
                if beenden:
                    print("Spieler 1 hat gewonnen!")
                    break
            while not ueberpruefe_spielzug_spieler2:
                spielzug_spieler_2 = self.spieler2.spielzug(self.__gui)
                ueberpruefe_spielzug_spieler2 = self.__spielregeln.volleSpalte(self.__feld, spielzug_spieler_2)

            self.__feld.setFelder(spielzug_spieler_2)
            self.__gui.printSpielfeld(self.__feld)
            if self.__spielregeln.voll(self.__feld):
                print("Das Spielfeld ist voll. UNENTSCHIEDEN!")
                break
            if self.__spielregeln.gewonnen(self.__feld):
                print("Spieler 2 hat gewonnen!")
                break


if __name__ == '__main__':
    game = DasSpiel()
    game.spielStart()
