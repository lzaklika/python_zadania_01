# Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
# ​
# Logikę obliczania liczby dni wydziel do osobnej funkcji.
# ​
# **Wersja A**
# Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
# ​
# **Wersja B (trudniejsza)**
# Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.

def czy_rok_przestepny(rok: int) -> bool:
    """

    :param rok: liczba odpowiadająca za podany rok (int)
    :return: zwrot True jeśli jest przestępny, lub False jeśli przestępny nie jest
    """
    if type(rok) != int:
        wynik = ValueError
    if rok % 4 == 0:
        wynik = True
    else:
        wynik = False

    return wynik

def ile_dni_ma_miesiac(nazwa: str) -> int:
    """

    :param nazwa: przyjmuje napis wprowadzony przez użytkownika bez zmieniania wielkości liter
    :return: liczba dni zależnie od wprowadzonego miesiąca, lub Error w przypadku niezidentyfikowania nazwy miesiąca
    """
    wynik = 0

    if nazwa.lower() == "luty":
        if czy_rok_przestepny(rok) == True:
            return 29
        else:
            return 28

    for miesiac, liczba_dni in miesiace:

        if miesiac == nazwa.lower():
            wynik = liczba_dni
            return wynik

    if wynik == 0:
        print("Podałeś nieprawidłową nazwę miesiąca!")
        return ValueError


miesiace = [("styczeń", 31), ("luty", 28), ("marzec", 31), ("kwiecień", 30), ("maj", 31), ("czerwiec", 30), ("lipiec", 31), ("sierpień", 31), ("wrzesień", 30), ("październik", 31), ("listopad", 30), ("grudzień", 31)]


napis = str(input("Podaj nazwę miesiąca, aby dowiedzieć się ile ma on dni: "))

if napis.lower() == "luty":
    rok = int(input("Musisz podać jeszcze rok: "))
print(ile_dni_ma_miesiac(napis))

#### TESTY ####

def test_czy_rok_przestepny():
    wartosci_testowe = [(0, True), (2020, True), (18728, True), (1990, False), (1991, False), (1992, True), (1993, False), (1994, False), (-168, True), (-169, False), (-170, False), (456.7, ValueError)]

    for rok, wynik in wartosci_testowe:
        assert czy_rok_przestepny(rok) == wynik

def test_ile_dni_ma_miesiac():
    assert ile_dni_ma_miesiac(5) == ValueError
    assert ile_dni_ma_miesiac("styczeń") == 31
    assert ile_dni_ma_miesiac("LIStopAD") == 30
    assert ile_dni_ma_miesiac("nie podam nazwy miesiąca") == ValueError
    # assert ile_dni_ma_miesiac("Luty") == 28
