# Test

Überprüft wurden die Funktionen der Klassen Spielfeld, GUI, Spielmodus sowie Spielregeln.
Der erste Test namens test_Spielmodus überprüft ob der Spieler eine gültige Auswahl 
zu Beginn des Spiels trifft. Wählt man etwas anderes als 1 oder 2 aus, bekommt man einen
Error. Der Test test_Spielfeld überprüft, ob die Spielsteine korrekt gesetzt werden.
Der Test test_gueltige_Spalte überprüft, ob die Eingabe des Spielers valid ist (1-7).
Weiters wurde ein Test erstellt, welcher mittels einer Schleife prüft, ob das Spielfeld voll ist.
Der Test für die Funktion test_gewonnen_vertikal überprüft die Funktion gewonnen nach 4 vertikalen Steinen.
Der Test für die Funktion test_gewonnen_horizontal macht dasselbe nach 4 horizontalen Steinen.
Die beiden Tests für die Funktionen test_gewonnen_diagonal_links_oben sowie test_gewonnen_diagonal_rechts_oben
überprüfen die Funktion gewonnen jeweils nach 4 Steinen diagonal von links oben nach rechts unten sowie diagonal 
von rechts oben nach links unten. Anschließend wurde ein Test für die Funktion printSpielfeld geschrieben, welcher
anhand von eines leeren Spielfeldes ebendiese Funktion überprüft. Wichtig war es uns auch einen Case zu testen,
in welcher das Spielfeld voll ist. Zuallerletzt wurde die Funktion def test_spielstart geschrieben. Die Funktion
simuliert das Spiel von 2 Computerspielern, ohne das Spielfeld auszugeben. Dabei können je nach Häufigkeit der Simulation
immer mehr Fehler gefunden werden.
Aufgrund jener Funktionen, die einen Input erfordern, konnten wir 100 Prozent Test Coverage nicht erreichen.
Mit den Methoden, die wir in der Lehrveranstaltung SEM gelernt haben, war eine 100 Prozentige Coverage nicht
realisierbar.