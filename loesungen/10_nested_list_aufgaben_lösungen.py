# Erstelle eine list tic
tic = []
# Füge tic eine Liste mit den werten 'l','l','l' hinzu
# Füge tic eine 2. liste mir den werten 'k','k','k' hinzu
# Füge tic eine 3. liste mir den werten 'b','b','b' hinzu
tic.append(['l', 'l', 'l'])
tic.append(['k', 'k', 'k'])
tic.append(['b', 'b', 'b'])
print(tic)
# Printe jede unterliste in einer Zeile aus
# ['l', 'l', 'l']
# ['k', 'k', 'k']
# ['b', 'b', 'b']
print(tic[0])
print(tic[1])
print(tic[2])
print('------------------------------')
# ändere die liste wie folgt ab
# ['x', 'l', 'l']
# ['k', 'x', 'k']
# ['b', 'b', 'x']
tic[0][0] = 'x'
tic[1][1] = 'x'
tic[2][2] = 'x'
print(tic[0])
print(tic[1])
print(tic[2])
# ändere die liste wie folgt ab
# ['x', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
print('------------------------------')
tic[0][1] = 'o'
tic[0][2] = 'o'
tic[1][0], tic[1][-1] = 'x', 'o'
tic[2][0], tic[2][1], tic[2][2] = 'o', 'x', 'o'
print(tic[0])
print(tic[1])
print(tic[2])
# ändere die liste wie folgt ab
# ['o', 'o', 'o']
# ['x', 'x', 'o']
# ['o', 'x', 'o']
print('------------------------------')
tic[0][0] = 'o'
print(tic[0])
print(tic[1])
print(tic[2])
# schriebe ein Programm das 2 Zahlen zwischen 1 und 3 und einem Buchstaben vom user fordert
# Anschliessend soll der Wert mit der Pos der zwei Zahlen mit den Buchstaben überschrieben werden
# und die Liste wie in der vorherigen Aufgabe ausgegeben werden
# y
# c['o', 'o', 'o']
# b['x', 'x', 'o']
# a['o', 'x', 'o']
#    1    2    3  x


# zahl1 = input('Zahl fuer x')
# zahl2 = input('Zahl fuer y')
# zahl1 = int(zahl1)
# zahl2 = int(zahl2)
# zeichen = input('zeichen')
# print('--------------------------')
# print(tic[0])
# print(tic[1])
# print(tic[2])
# if zahl2 == 'a':
#     zahl2 = 2
# elif zahl2 == 'b':
#     zahl2 = 1
# elif zahl2 == 'c':
#     zahl2 = 0


# tic[zahl2][zahl1-1] = zeichen
print('--------------------------')
print(tic[0])
print(tic[1])
print(tic[2])
# if y_wert == 1:
#     y_wert = 2
# elif y_wert == 2:
#     y_wert= 1
# elif y_wert == 3:
#     y_wert = 0


# Beispiel Zahl1 = 3 Zahl2 = 2 Buchstabe = p
# 1['o', 'o', 'o']
# 2['x', 'x', 'p']
# 3['o', 'x', 'o']

# Zähle alle "o" in der mittleren Liste
tic[1][0] = 'o'
print('--------------------------')
print('1',tic[0])
print(tic[1])
print(tic[2])
x = 0
if tic[1][0] == 'o':
    x += 1
if tic[1][1] == "o":
    x += 1
if tic[1][2] == "o":
    x += 1

print(x)

tic[1][0] = 'o'
tic[1][1] = 'o'
print('--------------------------')
print(tic[0])
print(tic[1])
print(tic[2])

# Schreib eine If anweisung die 'Sieg' ausgibt wenn das Zeichen auf pos 1.1 das selbe ist wie auf pos 2.2 und 3.3
if tic[0][0] == tic[1][1] and tic[1][1] == tic[2][2]:
    print('\033[0;32mSieg')