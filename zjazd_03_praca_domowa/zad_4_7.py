# ​
# ### Zadanie 4.7 | Ogłoszenia / dziedziczenie
# ​
# Do zadania z klasą `Ogloszenie` dodaj kolejne kolejne klasy, które po niej dziedziczą.
# ​
# `OgloszenieSamochodowe` – dziedziczy z `Ogloszenie` i dodatkowo określa cechy
# sprzedawanego samochodu jak model, markę, rok produkcji, przebieg, pojemność,
# moc i rodzaj paliwa.

# `OgloszenieMieszkaniowe` – też dziedziczy z `Ogloszenie`,
# a dodatkowo cechy sprzedawanego mieszkania / domu: miejscowość, metraż, liczba pokoi.

from zjazd_03_praca_domowa.zad_4_1 import Advertisement

class OgloszenieSamochodowe(Advertisement):

    def __init__(self, title: str, description: str, price: float, currency: str, contact_mail: str, contact_phone: int):
        super().__init__(title, description, price, currency, contact_mail, contact_phone)
        self.model = ""
        self.marka = ""
        self.rok_produkcji = 0
        self.przebieg = 0
        self.pojemnosc = 0
        self.moc = 0
        self.rodzaj_paliwa = ""

    def __str__(self):
        return (f"{self.title}\n\n{self.description}\nMODEL: {self.model}\nMARKA: {self.marka}\nROK PRODUKCJI: {self.rok_produkcji}\nPRZEBIEG: {self.przebieg}\nPOJEMNOŚĆ: {self.pojemnosc} l\nMOC: {self.moc} kW\nRODZAJ PALIWA: {self.rodzaj_paliwa}\nCENA: {self.price} {self.currency}\nKONTAKT:\n{self.contact_phone}\n{self.contact_mail}")


auto_sample = OgloszenieSamochodowe("SPRZEDAM AURISA", "Mam na sprzedaż samochód!", 30000, "PLN", "sale@sale.gru", "123321321", "Auris", "Toyota", 2015, 65000, 50, 97, "Pb95")
print(auto_sample)
