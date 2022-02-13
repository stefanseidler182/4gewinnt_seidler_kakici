from collections import defaultdict

# Key = (spalte, zeile), Value = 'O' oder 'X'
spielfeld = {}

# Unser Spielfeld hat 7 Spalten und 6 Zeilen, daraus ergibt sich die Anzahl der Zellen
SPALTEN = 7
ZEILEN = 6
ZELLEN = SPALTEN * ZEILEN
# Die Richtungen dienen dazu, zu überprüfen, ob ein Spieler (in eine bestimmte Richtung) gewonnen hat.
RICHTUNGEN = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
# pos2Index geben wir eine Position(Key-Spalte, Zeile) und für diese Position vergeben wir einen
# Value (Index der betroffenen Quads)
pos2Index = defaultdict(list)

"""
def spielstart():
    spieler = int(input('Gibt 1, für Mensch vs. Mensch oder 2 für Mensch vs. Computer, ein!'))
    if spieler == 1:
        "Mensch vs. Mensch"
        return True
    elif spieler == 2:
        "Mensch vs. Computer"
        return True
    else:
        print("Falsche Eingabe!")
        return False
"""
"""
Die KI hat die folgende Funktionsweise:
Zuerst werden alle gültigen Quads gefunden. D.h. Es werden von allen Positionen(ZELLEN), in alle Richtungen
überprüft, ob es ein mögliches Quad gibt, um zu gewinnen.
"""


def quadPositionen(position, richtung):
    positionen = set()
    spalte, zeile = position
    spaltenrichtung, zeilenrichtung = richtung
    neue_spalte, neue_zeile = spalte + spaltenrichtung * 3, zeile + zeilenrichtung * 3
    if neue_spalte < 0 or neue_spalte >= SPALTEN or neue_zeile < 0 or neue_zeile >= ZEILEN:
        return False
    for i in range(4):
        positionen.add((spalte + spaltenrichtung * i, zeile + zeilenrichtung * i))
    return positionen


# Diese Funktion ermittelt die Quads
def quadsErmitteln():
    zaehler = 0
    quads = {}
    bekannte_positionen = set()
    for i in range(ZELLEN):
        for richtung in RICHTUNGEN:
            position = (i % SPALTEN, i // SPALTEN)
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


def findeTiefsteZeile(spalte):
    for zeile in reversed(range(ZEILEN)):
        if (spalte, zeile) not in spielfeld:
            return zeile


# Diese Funktion überprüft, ob die eingegebene Spalte gültig ist, der Wert für die Spalte darf 0-6 sein.
def spalteGueltig(spalte):
    if (spalte, 0) in spielfeld:
        return False
    if 0 <= spalte < 7:
        return True


# Diese Funktion gibt das aktuelle Spielfeld aus. Ein '.' steht für ein leeres Feld, in 'O' für einen Stein von
# Spieler 1 und ein 'X' für einen Stein von Spieler2.
def printSpielfeld():
    for i in range(ZELLEN):
        if i % SPALTEN == 0:
            print()
        position = (i % SPALTEN, i // SPALTEN)
        if position in spielfeld:
            print(spielfeld[position], end=' ')
        else:
            print('.', end=' ')
    print()


# Diese Funktion ersetzt die Funktion gewonnen
def steinSetzen(position, spieler):
    sieg = False
    spielfeld[position] = 'O' if spieler else 'X'
    for i in pos2Index[position]:
        quads[i][spieler] += 1
        if quads[i][spieler] == 4:
            sieg = True
    return sieg


# Diese Funktion dient der KI zum löschen von Zügen die sie durchprobiert
def steinLoeschen(position, spieler):
    del spielfeld[position]
    for i in pos2Index[position]:
        quads[i][spieler] -= 1


# Diese Funktion bewertet das Spielfeld (die gesetzen Steine)
def bewerten():
    score = 0
    for pos in spielfeld:
        for i in pos2Index[pos]:
            gelbe, rote = quads[i]
            if gelbe > 0 and rote > 0: continue
            score += rote * 10
            score -= gelbe * 10
    return score


# Diese Funktion liefert alle möglichen Züge
def zugliste():
    zuege = []
    for spalte in range(SPALTEN):
        if not spalteGueltig(spalte):
            continue
        zeile = findeTiefsteZeile(spalte)
        zuege.append((spalte, zeile))
    return zuege


# Diese Funktion ist für einen echten zweiten Mitspieler bestimmt
def human(spieler):
    while True:
        spalte = int(input('In welche Spalte willst du setzen(0-6)?'))
        if spalteGueltig(spalte):
            break
    zeile = findeTiefsteZeile(spalte)
    sieg = steinSetzen((spalte, zeile), spieler)
    return sieg


# Diese Funktion ist für die KI bestimmmt, dieser nimmt den zug mit dem höchsten score
def computer(spieler):
    bewertete_zuege = []
    for zug in zugliste():
        sieg = steinSetzen(zug, spieler)
        score = minimax(4, -999999, 999999, spieler, sieg)
        steinLoeschen(zug, spieler)
        bewertete_zuege.append((score, zug))
    bewertete_zuege.sort(reverse=spieler)
    score, bester_zug = bewertete_zuege[0]
    sieg = steinSetzen(bester_zug, spieler)
    print(bewertete_zuege)
    print(f'Spieler {1 if spieler else 2} setzt {bester_zug} mit der Bewertung {score}')
    return sieg


def minimax(tiefe, alpha, beta, spieler, sieg):
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


quads = quadsErmitteln()

spieler = True

if __name__ == '__main__':
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
    while True:
        printSpielfeld()
        if spieler:
            sieg = human(spieler)
        else:
            sieg = computer(spieler)
        if sieg:
            printSpielfeld()
            print('GEWONNEN!!!')
            break
        spieler = not spieler
