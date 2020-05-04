import math

import pytest


def wczytaj_float():
    """

    :return: przyjmuje wartość od użytkownika i zwraca ją jako float
    """
    wartosc = float(input())
    return wartosc


def wczytaj_int():
    """

    :return: przyjmuje wartość od użytkownika i zwraca ją jako int
    """
    wartosc = int(input())
    return wartosc


# def stopy_na_metry() -> float:
#     """
#
#     :return: zwraca podana wartośc przeliczoną na metry
#     """
#     przelicznik = 0.3048
#     print("Podaj wartość wyrażoną w stopach, którą algorytm przeliczy na metry:")
#     stopy_wartosc = wczytaj_float()
#     metry_wartosc = stopy_wartosc * przelicznik
#     print (f"Podana liczba stóp ({stopy_wartosc}), to {metry_wartosc} metrów")
#     return metry_wartosc


def max(liczba1: float, liczba2: float) -> float:
    """

    :param liczba1: pierwsza wczytana liczba typu float
    :param liczba2: druga podana liczba typu float
    :return: wartość maksymalna z podanych liczb (float)
    """
    if liczba1 > liczba2:
        max = liczba1
        print(f"Wartośc wyższa, to: {max}")
    elif liczba1 < liczba2:
        max = liczba2
        print(f"Wartośc wyższa, to: {max}")
    else:
        max = liczba1
        print("Podane liczby są równe!")
    return max


def srednia(liczba1: float, liczba2: float) -> float:
    """

    :param liczba1: pierwsza wczytana liczba typu float
    :param liczba2: druga podana liczba typu float
    :return: wartość średnia tych liczb (float)
    """
    suma = liczba1 + liczba2
    wynik = suma / 2
    return wynik


def pole_kola(promien: float) -> float:
    """

    :param promien: wartość przyjęta jako promień okręgu (float)
    :return: wartość pola (float)
    """
    if promien < 0:
        print("Promień nie może być ujemny!")
        return ValueError
    wynik = math.pi * promien ** 2
    print(f"Pole koła o zadanym promieniu {promien} wynosi: {round(wynik, 2)}")
    return wynik


def bmi(masa: float, wzrost_cm: int) -> float:
    """

    :param masa: wartość odpowiedzalna za wagę (float)
    :param wzrost_cm: wartość odpowiedzialna za wzrost podana w cebtymatrach (int)
    :return: wartość wskaźnika BMI dla podanych wartości (float)
    """
    wzrost_m = wzrost_cm / 100
    wynik = masa / wzrost_m ** 2
    print(f"Wskaźnik BMI dla człowieka o wzroscie {wzrost_m}m i wadze {masa}kg wynosi: {round(wynik, 2)}")
    return wynik


def pole_trojkata(bok1: float, bok2: float, bok3: float) -> float:
    """

    :param bok1: wartość pierwszego boku trójkąta
    :param bok2: wartość drugiego boku trójkąta
    :param bok3: wartość trzeciego boku trójkąta
    :return: obliczone pole trójkąta (float)
    """
    if bok1 + bok2 < bok3 or bok1 + bok3 < bok2 or bok2 + bok3 < bok1:
        print("Podany trójkąt nie istnieje!")
        return ValueError
    else:
        p = (bok1 + bok2 + bok3) / 2
        wynik = math.sqrt(p * (p - bok1) * (p - bok2) * (p - bok3))
        print(f"Pole trojakta z zdanych bokow o długości: {bok1}, {bok2}, {bok3}, wynosi: {round(wynik, 2)}")
    return wynik

def kilometry_na_mile(wartosc_km: float) -> float:
    """

    :param wartosc_km: podana przez użytkownika wartość kilometrów
    :return: przeliczona przez algorytm wartość wyrażona w milach
    """
    przelicznik = 0.621371192
    wartosc_mila = wartosc_km * przelicznik
    print(f"{wartosc_km}km = {round(wartosc_mila, 2)} mil")


def mile_na_kilometry(wartosc_mile: float) -> float:
    """

    :param wartosc_mile: podana przez użytkownika wartość mil
    :return: przeliczona przez algorytm wartość w kilometrach
    """
    przelicznik = 1.609344
    wartosc_km = wartosc_mile * przelicznik
    print(f"{wartosc_mile}km = {round(wartosc_km, 2)} mil")


# stopy_na_metry()

print("Podaj dwie liczby, żeby sprawdzić, która jest większa:")
max(wczytaj_float(), wczytaj_float())

print(f"Srednia wartosc z liczb 5 i 2, to: {srednia(5, 2)}")

print(f"Podaj promien kola")
pole_kola(wczytaj_float())

print("Teraz obliczymy BMI. Podaj wagę")
masa = wczytaj_float()
print("... i wzrost w cm")
wzrost_cm = wczytaj_int()
bmi(masa, wzrost_cm)

pole_trojkata(4, 5.5, 7)

kilometry_na_mile(50)

mile_na_kilometry(50)

#### TESTY ####

def test_max():
    assert max(5, 2) == 5
    assert max(5, 12.5) == 12.5
    assert max(11.45423, 11.45422) == 11.45423
    assert max(0, -5) == 0
    assert max(2, 2) == 2
    assert max(-33, -32.54) == -32.54


def test_srednia():
    assert srednia(5, 2) == 3.5
    assert srednia(0, 0) == 0
    assert srednia(-5, -50) == -27.5
    assert srednia(-5, 10) == 2.5


def test_pole_kola():
    assert pole_kola(0) == 0
    assert pole_kola(1) == math.pi
    assert pole_kola(5) == 25 * math.pi
    with pytest.raises(ValueError):
        pole_kola(-1)
        pole_kola(-0.5)
        pole_kola(-543)

# def test_pole_trojkata():
#     assert pole_trojkata(3, 4, 5) ==