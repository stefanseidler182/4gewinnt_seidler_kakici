from collections import defaultdict
# Key = (spalte, zeile), Value = 'O' oder 'X'
spielfeld = {}

# Unser Spielfeld hat 7 Spalten und 6 Zeilen, daraus ergibt sich die Anzahl der Zellen
SPALTEN = 7
ZEILEN = 6
ZELLEN = SPALTEN * ZEILEN
# Die Richtungen dienen dazu, zu überprüfen, ob ein Spieler (in eine bestimmte Richtung) gewonnen hat.
RICHTUNGEN = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
# pos2Index geben wir eine Position(Key-Spalte,Zeile) und für diese Position vergeben wir einen
# Value (Index der betroffenen Quads)
pos2Index = defaultdict(list)

def quadPositionen(pos, richtung):
    positionen = set()
    sp, ze = pos
    rsp, rze = richtung
    neue_sp, neue_ze = sp + rsp*3, ze+rze*3
    if neue_sp < 0 or neue_sp >= SPALTEN or neue_ze < 0 or neue_sp >= ZEILEN:
        return False
    for i in range(4):
        positionen.add((sp+rsp*i, ze+rze*i))
    return positionen

# Diese Funktion ermittelt die Quads

def quadsErmitteln():
    zähler = 0
    quads = {}
    bekannte_positionen = set()

    for i in range(ZELLEN):
        for richtung in RICHTUNGEN:
            pos = (i % SPALTEN, i // SPALTEN)
            positionen = quadPositionen(pos, richtung)
            if not positionen or positionen in bekannte_positionen: continue
            quads[zähler] = [0,0]   # Anzahl der gelben[0], roten[1] Steine im Quad
            for position in positionen:
                pos2Index[position].append([zähler])
            bekannte_positionen.add(frozenset(positionen))
            zähler += 1
    return quads

quads = quadsErmitteln()

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

# Diese Funktion ersetzt die Funktion gewonnen
def steinSetzen(pos, spieler):
    win = False
    spielfeld[pos] = 'O' if spieler else 'X'
    for i in pos2Index[pos]:
        quads[i][spieler] += 1
        if quads[i][spieler] == 4:
            win = True
    return win

# Diese Funktion dient der KI zum löschen von Zügen die sie durchprobiert
def steinLöschen(pos, spieler):
    del spielfeld[pos]
    for i in pos2Index[pos]:
        quads[i][spieler] -= 1

#Diese Funktion bewertet das Spielfeld (die gesetzen Steine)
def bewerten():
    score = 0
    for pos in spielfeld:
        for i in pos2Index[pos]:
            gelbe, rote = quads[i]
            if gelbe > 0 and rote > 0: continue
            score += rote*10
            score -= gelbe*10
    return score

# Diese Funktion liefert alle möglichen Züge
def zugliste():
    züge = []
    for spalte in range(SPALTEN):
        if not spalteGueltig(spalte): continue
        zeile = findeTiefsteZeile(spalte)
        züge.append((spalte,zeile))
    return züge

#Diese Funktion ist für einen echten zweiten Mitspieler bestimmt
def human(spieler):
    while True:
        spalte = int(input('In welche Spalte willst du setzen(0-6)?'))
        if spalteGueltig(spalte):
            break
    zeile = findeTiefsteZeile(spalte)
    win = steinSetzen((spalte, zeile), spieler)
    return win

#Diese Funktion ist für die KI bestimmmt, dieser nimmt den zug mit dem höchsten score
def computer(spieler):
    bewertete_züge = []
    for zug in zugliste():
        win = steinSetzen(zug, spieler)
        score = minimax(4, -999999, 999999, spieler, win)
        steinLöschen(zug, spieler)
        bewertete_züge.append((score,zug))
    bewertete_züge.sort(reverse=spieler)
    score, bester_zug = bewertete_züge[0]
    win = steinSetzen(bester_zug, spieler)
    print(bewertete_züge)
    print(f'Spieler {1 if spieler else 2} setzt {bester_zug} mit der Bewertung {score}')
    return win


def minimax(tiefe, alpha, beta, spieler, win):
    if win:
        return 999999+tiefe if spieler else -999999-tiefe
    if tiefe == 0 or len(spielfeld) == ZELLEN:
        return bewerten()
    spieler = not spieler
    value = -999999 if spieler else 999999
    for zug in zugliste():
        win = steinSetzen(zug, spieler)
        score = minimax(tiefe-1, alpha, beta, spieler, win)
        steinLöschen(zug, spieler)
        if spieler:
            value = max(value, score)
            alpha = max(value, alpha)
        else:
            value = min(value, score)
            beta = min(value, beta)
        if alpha >= beta:
            break
        return value



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
        print(spielfeld)
        if spieler:
            win = human(spieler)
        else:
            win = computer(spieler)
        if win:
            spieler = not spieler

