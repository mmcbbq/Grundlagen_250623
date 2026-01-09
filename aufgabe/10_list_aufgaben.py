# Erstellen Sie eine Liste von 5 Städten, die Sie besuchen möchten.
city = ['Paris', 'Kyoto', 'Venedig', 'Sydney', 'New York City']
# Fügen Sie dann eine weitere Stadt hinzu und entfernen Sie die dritte Stadt aus der Liste.
city.append("Wien")
# city.insert(1,'Hamburg')
city.pop(2)
# Schließlich geben Sie die Liste der verbleibenden Städte aus.
print(city)

# Erstelle eine Liste super_liste mit folgenden Items: 20, 50.5, 'Hallo', True, 'Löschen', 'auf Wiedersehen'
super_liste = [20, 50.5, 'Hallo', True, 'Löschen', 'auf Wiedersehen', 'bin da']
# Ändere den Wert des ersten Elementes zu 95
super_liste[0] = 95
print(super_liste)
# Kopiere den Wert des 4 Items auf den 2 index
super_liste[2] = super_liste[3]
# Ändere das 4 Element zu False
super_liste[3] = False
# Füge das Element "999" an der letzten Stelle der Liste an
super_liste.append('999')
# Füge das Element "Nummer 5" an der 5 Stelle ein
super_liste.insert(4, 'Nummer 5')
# tauche das Element mit dem Index 0 und das Index 5
zwischen = super_liste[0]
super_liste[0] = super_liste[5]
super_liste[5] = zwischen
# Schreibe eine If anweisung die das Element 'bin da' löscht, wenn es vorhanden ist.
print(super_liste)
if 'bin da' in super_liste:
    super_liste.remove('bin da')
else:
    super_liste.append('bin da')
print(super_liste)
# Wenn das Element nicht vorhanden ist, soll es an letzter Stelle hinzugefügt werden

# copy die liste in die Variable list_copy
list_copy = super_liste.copy()
# Leere die Originalliste
super_liste.clear()
print(list_copy)
print(super_liste)
# Füge die letzten 3 Elemente der list_copy an die super_liste an.
super_liste.extend(list_copy[-3:])
# super_liste.append(list_copy[-2])
# super_liste.append(list_copy[-1])
print(super_liste)