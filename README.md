# Witzgram
Beim Starten des Programms wird eine GUI geöffnet.
## Witze anzeigen
Im oberen Teil des Fensters wird initial ein Witz des Tages angezeigt. Durch betätigen des Next-Buttons wird ein neuer Witz (aus JokeAPI Schnittstelle) angezeigt.
### Witze liken / disliken
Durch betätigen des Like-Buttons kann ein Witz in die lokale Datenbank gespeichert werden. Sollte der Witz unter "Favoriten" nochmals geliked werden, so wird die Anzahl der Likes in der DB inkrementiert, sodass sich die Reihenfolge der in Favoriten angezeigten Witze ändert. 
Durch betätigen des dislike Buttons wird die Like-Anzahl dekrementiert (sofern der Witz in der DB steht). Sollten 0 Likes erreicht sein wird der Witz aus der DB gelöscht. Wenn der Witz nicht in der DB steht hat der Dislike-Button keine Funktion.
### Kategory ändern
Mit Hilfe des Dropdown-Menüs kann die Kategory des Witzes ausgewählt werden. Der neue Witz wird erst nach nochmaligem betätigen des Next-Buttons angezeigt. 
Abhängig von der Kategory wird ein anderes Hintergrundbild angezeigt.
Die Favoriten-Kategorie enthält ausschließlich Witze aus der lokalen Datenbank.
## Witze bereitstellen
Im untere Teil des Fensters kann ein eigener Witz der lokalen Datenbank hinzugefügt werden, dieser wird gleichzeitig an den Betreiber eines Witze-Webservices weitergegeben, um den Umfang von diesem weiter zu erhöhen.
### Tags
Für das übergeben des Witzes an den Webservice müssen einige Tags abhängig vom Witz gesetzt werden.
### Kategory
Um den Witz speichern zu können braucht dieser eine Kategory
## Exit
Der Exit-Button bietet die Möglichkeit die aktuell in der lokalen DB befindlichen Witze persistent zu speichern, sodass diese bei erneutem Programmaufruf zur Verfügung stehen.
Um Datenverluste zu vermeiden ist der "Fenser schließen"-Knopf deaktiviert.

# Getting Started
Repsitory in lokales Dateisystem pullen.
Module aus requirements.txt installieren.
Terminal öffnen und mit cd zum neu erstellten Orner "Witzgram" navigieren.
Führe "python3 GUI.py" aus (Main-Programm)



