from typing import List
from random import randint

# Die Richtungen dienen dazu, zu überprüfen, ob ein Spieler (in eine bestimmte Richtung) gewonnen hat.

# pos2Index geben wir eine Position(Key-Spalte, Zeile) und für diese Position vergeben wir einen
# Value (Index der betroffenen Quads)


ZAEHLER = 0  # Diese Variable wird bei jedem Spielzug um eins erhöht.
REIHE = 5  # Diese Variable wird dazu benötigt, dass der geworfene Spielstein immer in die tiefste Zeile fällt.
RICHTUNGEN = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
# Die Richtungen dienen dazu, zu überprüfen, ob ein Spieler (in eine bestimmte Richtung) gewonnen hat.
SPIELER = 0  # Diese Variable dient dazu, die Spieler als Spieler 1 und 2 anzusprechen.


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

    def getFelder(self) -> List:
        """
        übermittelt das Spielfeld
        """
        return self.__felder

    def setFelder(self, spalte: int):
        """
        Setzt Spielstein in die jeweilige Spalte.
        Ziel der Funktion ist es, dass der gespielte Stein bis zum
        letztmöglichen Punkt fällt, und nicht z.B. in der ersten Zeile hängen bleibt.
        ________________________________________

        spalte: int
            Gibt die Spalte die vom Spieler ausgewählt wurde, um den Stein zu setzen
        """
        global REIHE, ZAEHLER
        self.__letzteSpalte = spalte
        geworfen = False
        REIHE = 5
        for liste in reversed(self.__felder):
            if not geworfen:
                if liste[spalte] == ".":
                    if (ZAEHLER % 2) == 0:
                        liste[spalte] = 'X'
                        ZAEHLER += 1
                    else:
                        liste[spalte] = '0'
                        ZAEHLER += 1
                    self.__letzteReihe = REIHE
                    geworfen = True
                elif liste[spalte] != ".":
                    REIHE -= 1
                    self.__letzteReihe = REIHE

    def getLetzteReihe(self) -> int:
        """
        Gibt jene Reihe an, die zuletzt im Spiel bespielt wurde.
        Die Zählung fängt bei 0 von der obersten Reihe an
        """
        return self.__letzteReihe

    def getLetzteSpalte(self) -> int:
        """
        Gibt jene Spalte an, die zuletzt im Spiel bespielt wurde.
        Die Zählung fängt bei 0 von links an
        """
        return self.__letzteSpalte


class GUI:
    """
    Die Klasse GUI umfasst alle Informationen bezüglich des
    Graphical User Interfaces.
    """

    def __init__(self):
        pass

    def printSpielfeld(self, feld: Spielfeld):
        """
        Gibt das Spielfeld aus
        """
        for liste in feld.getFelder():
            print(liste[0], liste[1], liste[2], liste[3], liste[4], liste[5], liste[6])

    def getSpielmodus(self) -> int:
        """
        Die Funktion fordert vom Spieler eine Eingabe.
        Je nach Eingabe wird ein von zwei Spielmodi ausgewählt.
        Die Aufforderung wird so lange wiederholt, bis die Eingabe valide ist. (Parameter 1 oder 2)
        """
        global SPIELER
        gueltigeModi = [1, 2]
        spielmodus = 0
        SPIELER += 1
        while spielmodus not in gueltigeModi:
            try:
                spielmodus = int(input(f'Spieler {SPIELER}: Bist du ein Mensch(1) oder ein Computer(2)'))
                if spielmodus not in gueltigeModi:
                    print(f'FALSCHE EINGABE! Bist du ein Mensch(1) oder ein Computer(2)')
                    continue
            except ValueError:
                print(f'FALSCHE EINGABE! Bist du ein Mensch(1) oder ein Computer(2)')
        return spielmodus

    def beenden(self):
        i = 0
        while i < 100:
            beenden = input(f'Möchtest du das Spiel beenden/aufgeben?(j/n)')
            if beenden == "j":
                return True
            elif beenden == "n":
                return False
            else:
                print(f'FALSCHE EINGABE! Gib "j"(beenden) oder "n"(weiterspielen) ein!')
                continue



    def erfasseSpielzug(self):
        """
        Die Funktion erfasst den eingegebenen Spielzug und überprüft dabei,
        ob es ein gültiger Spielzug ist. Falls der Spielzug nicht gültig ist,
        wird der Spieler zu einer erneuten Eingabe aufgefordert.
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
    Die Klasse Spielmodus umfasst alle Informationen bezüglich dem Spielmodus
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

    def __repr__(self):
        return f"Spielmodus: {self.__spielmodus}"

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
        pass

    def volleSpalte(self, feld: Spielfeld, spalte: int) -> bool:
        """
        Die Funktion überprüft, ob der jeweilige Spielzug des Spielers gültig ist.
        Falls eine Spalte bereits voll ist, wird der Spieler zu einer erneuten Eingabe
        aufgefordert.
        """
        spielfeld = feld.getFelder()
        if spielfeld[0][spalte] != ".":
            print("Spielzug nicht möglich. Spalte voll.")
            return False
        else:
            return True

    def voll(self) -> bool:
        """
        Diese Funktion überprüft nach jedem Spielzug, ob das Spielfeld voll ist. Der ZAEHLER wird bei jedem Spielzug,
        um eins erhöht.
        """
        if ZAEHLER < 42:
            return False
        else:
            return True

    def gewonnen(self, feld: Spielfeld) -> bool:
        """
        Die Funktion überprüft ob einer der Spieler das Spiel gewonnen hat.
        Die Funktion ruft das Spielfeld sowie die Zeile und Spalte des zuletzt geworfenen
        Spielsteins ab. Die erste Schleife überprüft in alle 8 Richtungen. Die if Bedingungen
        überprüfen ob 4 Steine im Array bzw im Spielfeld sind. Die zweite Schleife überprüft
        überprüft jeweils die Steine. Wenn der erste Stein gespielt ist, überprüft die Schleife
        den zweiten gesetzten Stein. Danach den dritten und vierten Stein. Wenn der vierte Stein
        True ist bricht man aus der Schleife raus und man bekommt den return Wert True.

        """
        spielfeld = feld.getFelder()
        zeile = feld.getLetzteReihe()
        spalte = feld.getLetzteSpalte()
        for i in range(8):
            vier_in_einer_reihe = True
            j = 1
            while j < 4:
                spaltenposition = spalte + RICHTUNGEN[i][0] * j
                zeilenposition = zeile + RICHTUNGEN[i][1] * j
                if zeilenposition > 5 or zeilenposition < 0 or spaltenposition > 6 or spaltenposition < 0:
                    j += 1
                    vier_in_einer_reihe = False
                    break
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
    initialisiert. Die spiel
    """

    def __init__(self):
        self.__feld = Spielfeld()
        self.__gui = GUI()
        self.__spielregeln = Spielregeln()
        self.spieler1 = Spielmodus(2)
        self.spieler2 = Spielmodus(2)

    def spielStart(self):
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
                    break
            while not ueberpruefe_spielzug_spieler1:
                spielzug_spieler_1 = self.spieler1.spielzug(self.__gui)
                ueberpruefe_spielzug_spieler1 = self.__spielregeln.volleSpalte(self.__feld, spielzug_spieler_1)

            self.__feld.setFelder(spielzug_spieler_1)
            self.__gui.printSpielfeld(self.__feld)
            if self.__spielregeln.voll():
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
                    break
            while not ueberpruefe_spielzug_spieler2:
                spielzug_spieler_2 = self.spieler2.spielzug(self.__gui)
                ueberpruefe_spielzug_spieler2 = self.__spielregeln.volleSpalte(self.__feld, spielzug_spieler_2)

            self.__feld.setFelder(spielzug_spieler_2)
            self.__gui.printSpielfeld(self.__feld)
            if self.__spielregeln.voll():
                print("Das Spielfeld ist voll. UNENTSCHIEDEN!")
                break
            if self.__spielregeln.gewonnen(self.__feld):
                print("Spieler 2 hat gewonnen!")
                break


if __name__ == '__main__':
    game = DasSpiel()
    game.spielStart()

"""
class Ki:
    def __init__(self):
        pass

    def quadsErmitteln(self):
        zaehler = 0
        quads = {}
        bekannte_positionen = set()
        for i in range(42):
            for richtung in RICHTUNGEN:
                position = (i % 7, i // 7)
                positionen = quadPositionen(position, richtung)
                if not positionen or positionen in bekannte_positionen:
                    continue
                quads[zaehler] = [0, 0]  # Anzahl der gelben[0], roten[1] Steine im Quad
                for position in positionen:
                    pos2Index[position].append([zaehler])
                bekannte_positionen.add(frozenset(positionen))
                # frozenset bewirkt, dass man einem set ein anderes set hinzufügen kann.
                zaehler += 1
        return quads

    def quadPositionen(self, position, richtung):
        positionen = set()
        spalte, zeile = position
        spaltenrichtung, zeilenrichtung = richtung
        neue_spalte, neue_zeile = spalte + spaltenrichtung * 3, zeile + zeilenrichtung * 3
        if neue_spalte < 0 or neue_spalte >= SPALTEN or neue_zeile < 0 or neue_zeile >= ZEILEN:
            return False
        for i in range(4):
            positionen.add((spalte + spaltenrichtung * i, zeile + zeilenrichtung * i))
        return positionen

    def steinLoeschen(self, position, spieler):
        del spielfeld[position]
        for i in pos2Index[position]:
            quads[i][spieler] -= 1

    def bewerten(self):
        score = 0
        for position in spielfeld:
            for i in pos2Index[position]:
                gelbe, rote = quads[i]
                if gelbe > 0 and rote > 0:
                    continue
                score += rote * 10
                score -= gelbe * 10
        return score

    def computer(self, spieler):
        bewertete_zuege = []
        for zug in zugliste():
            sieg = steinSetzen(zug, spieler)
            score = minimax(7, -999999, 999999, spieler, sieg)
            steinLoeschen(zug, spieler)
            bewertete_zuege.append((score, zug))
        bewertete_zuege.sort(reverse=spieler)
        score, bester_zug = bewertete_zuege[0]
        sieg = steinSetzen(bester_zug, spieler)
        print(f'Spieler {1 if spieler else 2} setzt {bester_zug} mit der Bewertung {score}')
        return sieg

    def minimax(self, tiefe, alpha, beta, spieler, sieg):
        if sieg:
            return 99999 + tiefe if spieler else -99999 - tiefe
        if tiefe == 0 or len(spielfeld) == ZELLEN:
            return bewerten()
        spieler = not spieler
        value = -999999 if spieler else 999999
        for zug in zugliste():
            sieg = steinSetzen(zug, spieler)
            score = minimax(tiefe - 1, alpha, beta, spieler, sieg)
            steinLoeschen(zug, spieler)
            if spieler:
                value = max(value, score)
                alpha = max(value, alpha)
            else:
                value = min(value, score)
                beta = min(value, beta)
            if alpha >= beta:
                break
        return value
        
"""

"""
Die KI hat die folgende Funktionsweise:
Zuerst werden alle gültigen Quads gefunden. D.h. Es werden von allen Positionen(ZELLEN), in alle Richtungen
überprüft, ob es ein mögliches Quad gibt, um zu gewinnen.

# Diese Funktion liefert alle möglichen Züge
def zugliste():
    zuege = []
    for spalte in range(SPALTEN):
        if not spalteGueltig(spalte):
            continue
        zeile = findeTiefsteZeile(spalte)
        zuege.append((spalte, zeile))
    return zuege


spieler = True
quads = quadsErmitteln()
while True:
    printSpielfeld()
    if spieler:
        sieg = human(spieler)
    else:
        sieg = human(spieler)
    if sieg:
        printSpielfeld()
        print('GEWONNEN!!!')
        break
    spieler = not spieler

'''
    Der Ablauf des Spiels schaut folgendermaßen aus:
    Zuerst wird das leere Spielfeld ausgegeben.
    Danach wählt der/die erste SpielerIn eine Spalte aus in die er/sie den Stein werfen will.
    Es wird überprüft, ob die Eingabe der Spalte gültig ist. (Werte von 0-6 sind erlaubt.)
    Danach wird überprüft ob, der/die SpielerIn gewonnen hat. (4 Steine in eine bestimmte Richtung.)
    Falls, dass nicht der Fall ist wirft der nächste Spieler einen Stein.
    Es wird wieder die Gültigkeit der Spalte und ob gewonnen wurde überprüft.
    Dies wird solange durchgeführt, bis ein Spieler gewonnen hat oder das Spielfeld voll mit Steinen ist.
    '''
"""
