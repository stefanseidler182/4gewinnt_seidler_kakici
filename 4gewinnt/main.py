# Key = (spalte, zeile), Value = 'O' oder 'X'
spielfeld = {}

# Unser Spielfeld hat 7 Spalten und 6 Zeilen, daraus ergibt sich die Anzahl der Zellen
SPALTEN = 7
ZEILEN = 6
ZELLEN = SPALTEN * ZEILEN
# Die Richtungen dienen dazu, zu überprüfen, ob ein Spieler (in eine bestimmte Richtung) gewonnen hat.
RICHTUNGEN = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


# Diese Funktion findet die Zeile, in die der Spielstein fällt.
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


# Diese Funktion überprüft, ob der jeweilige Spieler, der den letzten Stein geworfen hat, gewonnen hat.
def gewonnen(spieler):
    stein = 'O' if spieler else 'X'
    for pos in spielfeld:
        for richtung in RICHTUNGEN:
            vier_in_einer_reihe = True
            for i in range(4):
                spalte, zeile = pos
                delta_spalte, delta_zeile = richtung
                p1 = (spalte + delta_spalte * i, zeile + delta_zeile * i)
                if p1 in spielfeld and spielfeld[p1] == stein:
                    continue
                vier_in_einer_reihe = False
                break
            if vier_in_einer_reihe:
                return True


# Diese Funktion überprüft, ob das Spielfeld voll ist und gibt dann aus: UNENTSCHIEDEN
def voll(spieler):
    pass

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
        while True:
            spalte = int(input('In welche Spalte willst du setzen(0-6)?'))
            if spalteGueltig(spalte):
                break
        zeile = findeTiefsteZeile(spalte)
        print(spalte, zeile)
        spielfeld[(spalte, zeile)] = 'O' if spieler else 'X'
        if gewonnen(spieler):
            printSpielfeld()
            print('Gewonnen!!!')
            break
        spieler = not spieler
