# Schreibe eine rekursive Funktion power(x, n), die die Potenz x hoch n berechnet.
import math


def pow(x: int, n: int) -> int:
    if n == 1:
        return x
    return x * pow(x, n - 1)


print(pow(5, 5))
print(5 ** 5)
# Schreibe eine rekursive Funktion, die Summe aller Zahlen in einer gegebenen Liste berechnet

list_sum = [12, 13, 14, 15]


# return 12 + 13 +14 +15

def summe_rec(l: list) -> int:
    if len(l) == 1:
        return l[0]
    return l[0] + summe_rec(l[1:])


print(summe_rec(list_sum))
print(sum(list_sum))


# Schreibe eine rekursive Funktion, die die Fakultät einer Zahl n berechnet.


def faku(n: int) -> int:
    if n == 1:
        return 1
    return n * faku(n - 1)


print(faku(10))
print(math.factorial(10))


# Schreibe eine rekursive Funktion reverse_string(s), die eine Zeichenkette s umkehrt.
# abc
# return cba
#
def reverse_string(s: str) -> str:
    if len(s) == 1:
        return s
    return s[-1] + reverse_string(s[:-1])


print(reverse_string('lagerregal'))


# Schreibe eine rekursive Funktion is_palindrome(s), die überprüft, ob eine Zeichenkette s ein Palindrom ist.

# abda
# return Bool and Bool
def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print('--------------palindrom-------------')
print(is_palindrome('ann1a'))


# Schreibe eine rekursive Funktion count_consonants(s), die die Anzahl der Konsonanten in einer Zeichenkette s zählt.
# abc
# return 0 + 1 +1

def count_cons(s: str) -> int:
    if len(s) == 0:
        return 0
    if s[0].lower() not in 'aeiou' and  s[0].isalpha():
        return 1 + count_cons(s[1:])
    else:
        return 0 + count_cons(s[1:])


print(count_cons('abcccuie123'))
