# Design

Die erste Überlegung war es, uns die notwendigen Klassen für eine Implementierung
der Spielregeln, des Spielfeldes, der zwei Spielmodi, einem User Interface sowie 
eine Klasse welches das Spiel erstellt zu überlegen. Die Klasse Spielregeln werden die Regeln 
des Spiels festgelegt. Die Klasse Spielfeld umfasst alles, was für das Spielfeld benötigt wird.
Die Klasse Spielmodus wird festgelegt, ob es sich um einen menschlichen Gegenspieler, oder einen
Computer als Gegenspieler handelt. Für das User Interface wurde die Klasse GUI erstellt. 
Sie umfasst alle Informationen bezüglich des Graphical User Interfaces. Als Letztes die Klasse
DasSpiel, welche das Spiel erstellt.

Das Spiel fängt mit einer Abfrage nach einem Input an. Der Spieler muss sich entscheiden,
ob er gegen einen menschlichen Mitspieler, oder gegen den Computer spielen will. Vor jedem
Spielzug wird zunächst abgefragt, ob der Spieler das Spiel vorzeitig beenden möchte. Dies
hat zur Folge, dass der Gegenspieler automatisch gewinnt. Falls sich der Spieler dazu entscheidet
weiterzuspielen, wird er gefragt, in welcher Reihe er den Spielstein setzen möchte. Alle Eingaben,
welche sich außerhalb des Spielfeldes befinden würden, haben eine Warnung zur Folge. Werden 4 gleiche
Steine horizontal, vertikal oder diagonal gelegt, gewinnt derjenige Spieler bzw. der Computer. Da 
auch die Möglichkeit eines Unentschieden nicht ausgeschlossen werden kann, wurde dies in die
Funktion spielStart implementiert.