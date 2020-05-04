from typing import List, Any

import pytest


def suma(liczby: list) -> int:
    """

    :param liczby: lista liczb
    :return: suma liczb z listy; jeśli brak liczb w liście zwróci 0
    """

    suma = 0

    if len(liczby) == 0:
        print("Lista jest pusta!")

    for i in liczby:
        suma += i

    return suma


def srednia(liczby: list) -> float:
    """

    :param liczby: lista liczb
    :return: średnia wartośc liczb z listy; jeśli lista jest pusta zwróci None
    """

    if len(liczby) == 0:
        print("Lista jest pusta!")
        return

    wynik = suma(liczby) / len(liczby)
    return wynik


def max(liczby: list) -> int:
    """

    :param liczby: lista liczb
    :return: wartość maksymalna z podanej listy; jeśli lista pusta zwróci None
    """
    if len(liczby) == 0:
        print("Lista jest pusta!")
        return

    maksimum = liczby[0]

    for i in liczby:
        if i > maksimum:
            maksimum = i

    return maksimum


def roznica_min_max(liczby: list) -> int:

    """

    :param liczby: lista liczb
    :return: wartość różnicy pomiędzy maksymalną i minimalną wartością z zadanej listy; jeśli lista jest pusta zwróci 0
    """
    wynik = 0

    if len(liczby) == 0:
        print("Lista jest pusta!")
        return wynik

    maksimum = liczby[0]
    minimum = liczby[0]

    for i in liczby:
        if i > maksimum:
            maksimum = i
        elif i < minimum:
            minimum = i

    wynik = maksimum - minimum
    return wynik


def wypisz_wieksze(liczby: list, x: int) -> list:

    """

    :param liczby: lista liczb
    :param x: liczba calkowita
    :return: wszystkie liczby z listy, ktore sa wieksze od podanej liczby calkowitej (x); jesli lista pusta, to zwroci pusta listę
    """
    lista_wynikowa = []

    if len(liczby) == 0:
        print("Lista jest pusta!")
        return lista_wynikowa

    for i in liczby:
        if i > x:
            lista_wynikowa.append(i)

    return lista_wynikowa


def pierwsza_wieksza(liczby: list, x: int) -> int:

    """

    :param liczby: lista liczb
    :param x: liczba całkowita
    :return: pierwsza liczba z listy, która okaże się większa od liczby całkowitej (x); jeśli lista będzie pusta, program zwróci None
    """
    if len(liczby) == 0:
        print("Lista jest pusta!")
        return

    wynik = None

    for i in liczby:
        if i > x:
            wynik = i
        if wynik != None:
            return wynik


def suma_wiekszych(liczby: list, x: int) -> int:

    """

    :param liczby: lista liczb
    :param x: liczba całkowita
    :return: wartość sumaryczna wszystkich liczb z listy, które są większe od zadanej liczby całkowitej (x); w przypadku pustej listy zwróci None
    """
    if len(liczby) == 0:
        print("Lista jest pusta!")
        return None

    wynik = 0

    for i in liczby:
        if i > x:
            wynik += i

    return wynik


def wypisz_podzielne(liczby: list, x: int) -> list:

    """

    :param liczby: lista liczb
    :param x: liczba całkowita
    :return: lista liczb z listy, które są podzielne przez zadaną liczbę całkowitą (x); w przypadku otrzymania pustej listy zwróci pustą listę wyników
    """
    lista_wynikowa = []

    if len(liczby) == 0:
        print("Lista jest pusta!")
        return lista_wynikowa

    for i in liczby:
        if i % x == 0:
            lista_wynikowa.append(i)

    return lista_wynikowa


def pierwsza_podzielna(liczby: list, x: int) -> int:

    """

    :param liczby: lista liczb
    :param x: liczba całkowita
    :return: pierwsza liczba z listy, która będzie podzielna przez podaną liczbę całkowitą (x); w przypadku pustej listy zwróci None
    """
    if len(liczby) == 0:
        print("Lista jest pusta!")
        return None

    wynik = None

    for i in liczby:
        if i % x == 0:
            wynik = i
            return wynik
        # if wynik != 0:
        #     return wynik
    return wynik


def znajdz_wspolny(liczby1: list, liczby2: list) -> list:

    """

    :param liczby1: pierwsza lista liczb
    :param liczby2: druga lista liczb
    :return: lista wspólnych elementów; jeśli któraś z list będzie pusta, to program zwróci pustą listę
    """
    lista_wynikowa = []

    if len(liczby1) == 0 or len(liczby2) == 0:
        print("Jedna z list jest pusta! Brak wspólnych wartości.")
        return lista_wynikowa

    for i in liczby1:
        for j in liczby2:
            if i == j:
                lista_wynikowa.append(i)

    return lista_wynikowa






#################################################################


lista_liczb = [10, 20, 30, 40]
lista_liczb2 = [10, 25, 30, 45, 60, 120]
liczba = 20


print(">>> SUMA <<<")
print(suma(lista_liczb))
print()


print(">>> ŚREDNIA <<<")
print(srednia(lista_liczb))
print()


print(">>> MAX <<<")
print(max(lista_liczb))
print()


print(">>> RÓŻNICA MAX-MIN <<<")
print(roznica_min_max(lista_liczb))
print()


print(f">>> WYPISZ WIĘKSZE OD {liczba} <<<")
print(wypisz_wieksze(lista_liczb, liczba))
print()


print(f">>> PIERWSZA WIĘKSZA OD {liczba} <<<")
print(pierwsza_wieksza(lista_liczb, liczba))
print()


print(f">>> SUMA WIĘKSZYCH OD {liczba} <<<")
print(suma_wiekszych(lista_liczb, liczba))
print()


print(f">>> WYPISZ PODZIELNE PRZEZ {liczba} <<<")
print(wypisz_podzielne(lista_liczb, liczba))
print()


print(f">>> PIERWSZA PODZIELNA PRZEZ {liczba} <<<")
print(pierwsza_podzielna(lista_liczb, liczba))
print()


print(f">>> ZNAJDŹ WSPÓLNY ELEMENT <<<")
print(znajdz_wspolny(lista_liczb, lista_liczb2))
print()


#### TESTY ####



def test_czy_puste():
    lista_pusta = []
    liczba = 20

    assert suma(lista_pusta) == 0
    assert srednia(lista_pusta) is None
    assert max(lista_pusta) is None
    assert roznica_min_max(lista_pusta) == 0
    assert wypisz_wieksze(lista_pusta, liczba) == []
    assert pierwsza_wieksza(lista_pusta, liczba) is None
    assert suma_wiekszych(lista_pusta, liczba) is None
    assert wypisz_podzielne(lista_pusta, liczba) == []
    assert pierwsza_podzielna(lista_pusta, liczba) is None
    assert znajdz_wspolny(lista_pusta, lista_liczb2) == []


def test_jeden_element():
    lista_jeden_element = [10]
    liczba = 20

    assert suma(lista_jeden_element) == lista_jeden_element[0]
    assert srednia(lista_jeden_element) == lista_jeden_element[0]
    assert max(lista_jeden_element) == lista_jeden_element[0]
    assert roznica_min_max(lista_jeden_element) == 0
    assert wypisz_wieksze(lista_jeden_element, liczba) == []
    assert pierwsza_wieksza(lista_jeden_element, liczba) is None
    assert suma_wiekszych(lista_jeden_element, liczba) == 0
    assert wypisz_podzielne(lista_jeden_element, liczba) == []
    assert pierwsza_podzielna(lista_jeden_element, liczba) is None
    assert znajdz_wspolny(lista_jeden_element, lista_liczb2) == [10]


def test_parametr_zero():
    liczba = 0

    assert wypisz_wieksze(lista_liczb, liczba) == [10, 20, 30, 40]
    assert pierwsza_wieksza(lista_liczb, liczba) == 10
    assert suma_wiekszych(lista_liczb, liczba) == 100
    with pytest.raises(ZeroDivisionError):
        wypisz_podzielne(lista_liczb, liczba)
        pierwsza_podzielna(lista_liczb, liczba)
