# ### Zadanie 4.4 | Zbiornik
# ​
# Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody`
# (z początkową wartością 0).
# ​
# Niech ta klasa ma metody `dolej` i `odlej`.
# Obie metody niech przyjmują argument `ile` i niech odpowiednio dodają
# lub odejmują tę liczbę do atrybutu `ilosc_wody`. Niech nie da się odlać więcej wody,
# niż jest w zbiorniku.
# ​
# Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis
# `zbiornik z (ileś tam) litrami wody`.
# ​
# Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`.
# Metoda dolej oprócz argumentu `ile` powinna też przyjmować argument `temperatura`
# oznaczający temperaturę dolewanej wody. Dolanie wody do zbiornika powinno powodować
# zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).

import pytest


class Zbiornik():
    def __init__(self):
        self.ilosc_wody = 0.0
        self.temperatura = 0.0


    def dolej(self, ile: float, temperatura_new: float):
        ilosc_wody_old = self.ilosc_wody
        ilosc_wody_new = self.ilosc_wody + ile
        temperatura_old = self.temperatura
        temperatura_mix = ((ilosc_wody_old * temperatura_old) + (ile * temperatura_new)) / (ile + ilosc_wody_old)

        self.ilosc_wody = ilosc_wody_new
        self.temperatura = temperatura_mix


    def odlej(self, ile: float) -> float:
        ilosc_wody_temp = self.ilosc_wody - ile

        if ilosc_wody_temp < 0:
            raise ValueError("Nie można odlać więcej wody niż jest w zbiorniku!")

        else:
            self.ilosc_wody -= ile


    def __str__(self) -> str:
        return f"Zbiornik z {self.ilosc_wody} litrami wody o temperaturze {self.temperatura} C."



def test_zbiornika():
    zb = Zbiornik()
    assert zb.ilosc_wody == 0

    zb.dolej(50, 15)
    assert zb.ilosc_wody == 50
    assert zb.temperatura == 15

    zb.dolej(50, 30)
    assert zb.ilosc_wody == 100
    assert zb.temperatura == 22.5

    zb.odlej(30)
    assert zb.ilosc_wody == 70

    with pytest.raises(ValueError):
        zb.odlej(100)

    zb.odlej(20)
    assert zb.ilosc_wody == 50