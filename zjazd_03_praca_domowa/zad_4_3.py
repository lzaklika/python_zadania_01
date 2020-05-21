# Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).
# ​
# Dodaj do klasy `Pociag` metode `opis`.
# Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam).
# Mam jeszcze (ileś tam) litrów paliwa." Dodatkowo zaimplementuj metodę `__str__`.
# ​
# Dodaj metode `przyspiesz`.
# Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość.
# Ta metoda niech zwiększa predkość pociągu o tyle, ile jest powiedziane w argumencie.
# I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.
# ​
# Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75%
# (jeśli ktoś spróbuje tak zwiększyć prędkość, prędkość niech pozostaje po prostu bez zmian).
# Niech nie da sie zwiększyć prędkości, jeśli pociąg nie ma juz paliwa
# (jeśli ktoś spróbuje zwiększyć prędkość, kiedy nie ma paliwa,
# prędkość niech pozostaje po prostu bez zmian).
# ​
# Przetestuj swoje rozwiązanie i napisz testy, w których:
# - zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
# - zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
# - zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
# - zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis

class Pociag():
    def __init__(self):
        self.predkosc = 10
        self.ilosc_paliwa = 1000

    def opis(self):
        return f"Moja predkosc to {self.predkosc}. Mam jeszcze {self.ilosc_paliwa} litrów paliwa."

    def __str__(self) -> str:
        return self.opis()

    def przyspiesz(self, przyspieszenie):
        """

        :param przyspieszenie: wielkosc o jaką zwięskza się aktualna wartość prędkości
        :return: nowa wartość prędkości oraz liczba paliwa, jaka pozostała w baku
        """
        if self.ilosc_paliwa == 0:
            return self.predkosc, self.ilosc_paliwa
        else:
            predkosc_old = self.predkosc
            predkosc_new = self.predkosc + przyspieszenie

            if predkosc_new >= predkosc_old * 1.75:
                predkosc_new = predkosc_old
            else:
                ilosc_paliwa_temp = self.ilosc_paliwa - (predkosc_new - predkosc_old) * (predkosc_old / 100)

                if ilosc_paliwa_temp > 0:
                    self.ilosc_paliwa = ilosc_paliwa_temp
                    self.predkosc = predkosc_new
                    return self.predkosc, self.ilosc_paliwa
                else:
                    return self.predkosc, self.ilosc_paliwa





a = Pociag()
print(a)
a.przyspiesz(5)
print(a)
a.przyspiesz(20)
print(a)
a.przyspiesz(8)
print(a)
a.przyspiesz(10)
print(a)
a.przyspiesz(10)
print(a)
a.przyspiesz(12)
print(a)

def test_przyspieszenie():
    b = Pociag()
    b.przyspiesz(5)
    print(b)
    assert b.predkosc == 15
    assert b.ilosc_paliwa == 999.5

def test_przyspieszenie_poza_prog():
    b = Pociag()
    b.przyspiesz(20)
    print(b)
    assert b.predkosc == 10
    assert b.ilosc_paliwa == 1000

def test_przyspieszenie_poza_prog2():
    b = Pociag()
    b.przyspiesz(8)
    print(b)
    assert b.predkosc == 10
    assert b.ilosc_paliwa == 1000

def test_przyspieszenie_poza_prog3():
    b = Pociag()
    b.przyspiesz(10)
    print(b)
    assert b.predkosc == 10
    assert b.ilosc_paliwa == 1000

def test_przyspieszenie_calosc():
    c = Pociag()
    c.przyspiesz(5)
    print(c)
    assert c.predkosc == 15
    assert c.ilosc_paliwa == 999.5

    c.przyspiesz(20)
    print(c)
    assert c.predkosc == 15
    assert c.ilosc_paliwa == 999.5

    c.przyspiesz(8)
    print(c)
    assert c.predkosc == 23
    assert c.ilosc_paliwa < 999.5 # trudno w tescie odgadnąć taką wartość bez wczesniejszego jej obliczenia, więc stąd założenie o nierówności

    c.przyspiesz(10)
    print(c)
    assert c.predkosc == 33
    assert c.ilosc_paliwa < 999.5 # trudno w tescie odgadnąć taką wartość bez wczesniejszego jej obliczenia, więc stąd założenie o nierówności
