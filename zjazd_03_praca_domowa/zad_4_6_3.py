# ### Zadanie 4.6 | Kółko i krzyżyk
# ​
# Stwórz klasę `PlanszaXO` - jej obiekty mają reprezentować stan planszy do gry w kółko i krzyżyk.
# ​
# Ma ona mieć metody:
# `dodaj_element(x: int, y: int, rodzaj_elementu)`
# W argumencie `rodzaj_elementu` będzie napis `"x"` lub `"y"`.
# Jeśli ruch jest nieprawidłowy, metoda powinna zwracać fałsz.
# ​
# `stan_gry()`
# Ta metoda ma zwracać liczbę oznaczającą stan gry
# (gra trwa, gra zakończona sukcesem krzyżyków, gra zakończona sukcesem kółek).
# ​
# `czyj_ruch()`
# Ta metoda ma powiedzieć, czyj ruch ma być teraz (kółek czy krzyżyków).
# ​
# Wyświetlenie obiektu tej klasy ma wypisać planszę.
# ​
# Użyj tej klasy do zrobienia gry w kółko i krzyżyk.

class PlanszaXO():

    def __init__(self):
        """
        Inicjacja zmiennych planszy
        """
        self.puste_pole = " "
        self.znak_x = "X"
        self.znak_o = "O"
        self.wielkosc_planszy = 3
        self.lista_1 = [self.puste_pole, self.puste_pole, self.puste_pole]
        self.lista_2 = [self.puste_pole, self.puste_pole, self.puste_pole]
        self.lista_3 = [self.puste_pole, self.puste_pole, self.puste_pole]
        self.plansza = [self.lista_1, self.lista_2, self.lista_3]
        self.ostatnio_uzyty_znak = ""


    def __str__(self):
        """
        Metoda wyświetlająca planszę
        :return: wydruk aktualnej planszy
        """
        plansza = ""
        plansza = plansza + ("-------\n")
        for i in range (0, self.wielkosc_planszy):
            plansza = plansza + ("|")
            for j in range (0, self.wielkosc_planszy):
                plansza = plansza + self.plansza[i][j] + "|"
            plansza = plansza + "\n"
            plansza = plansza + "-------\n"
        return plansza

    def sprawdz_element(self, x: int, y: int, rodzaj_elementu: str) -> bool:
        """
        Przed wpisaniem znaku na planszę, metoda sprwadza czy znak jest dopuszczony do gry oraz czy nie wpisano go poza planszą
        :param x: index kolumny
        :param y: index wiersza
        :param rodzaj_elementu: wprowadzony znak
        :return: dopuszczenie znaku i wspołrzędnych lub nie (True/False)
        """
        if rodzaj_elementu.lower() != "x" and rodzaj_elementu.lower() != "o":
            # raise ValueError("Należy wprowadzić 'X' lub 'O'!")
            print("Błąd rodzaju elementu")
            return False
        else:

            if x >= 0  and x <= self.wielkosc_planszy and y >= 0 and y <= self.wielkosc_planszy:
                return True
            else:
                # raise ValueError("Podano złe współrzędne!")
                print("Błąd wielkości planszy")
                return False

    def czy_puste_pole(self, x: int, y: int) -> bool:
        """
        Sprawdzenie czy pole nie jest już zajęte przez inny znak
        :param x: index kolumny
        :param y: index wiersza
        :return: Pole jest (True) lub zajęte (False)
        """
        if self.plansza[x][y] == self.puste_pole:
            return True
        else:
            return False


    def dodaj_element(self, x: int, y: int, rodzaj_elementu: str):
        """
        Metoda wpisująca na planszę znak podany w konsoli.
        :param x: index kolumny
        :param y: index wiersza
        :param rodzaj_elementu: wprowadzony znak
        :return: Update planszy, a w przypadku stwierdzenia wygranej również wydruk tej informacji. Po wpisaniu informacja o stanie gry.
        """
        if self.stan_gry() == 0:
            self.czyj_ruch()

            if self.sprawdz_element(x, y, rodzaj_elementu) == False:
                raise ValueError("Próbujesz wykonać zły ruch!")
                return False
            elif self.czy_puste_pole(x, y) == False:
                raise ValueError("Pole jest już zajęte! Możesz postawić znak tylko na pustym polu.")
                return False
            else:
                self.plansza[x][y] = rodzaj_elementu.upper()
                self.ostatnio_uzyty_znak = rodzaj_elementu.upper()
                # print(self.ostatnio_uzyty_znak)

            if self.czy_wygrana(self.ostatnio_uzyty_znak) == True:
                print(f"GRATULACJE! Wygrał gracz '{self.ostatnio_uzyty_znak}'!")
            print(f"STAN GRY: {self.stan_gry()}")

        else:
            print(f"Gra zakończona! Wygrał gracz '{self.ostatnio_uzyty_znak.upper()}'! Aby dodać kolejny element rozpocznij nową grę!")



    def czyj_ruch(self):
        """
        Metoda sprawdza czy jest ruch krzyżyków czy kółek
        :return: Wydruk napisu sugerującego kto ma teraz ruch
        """
        if self.ostatnio_uzyty_znak == self.znak_o:
            print("Teraz ruch krzyżyków. Postaw X!")
        elif self.ostatnio_uzyty_znak == self.znak_x:
            print("Teraz ruch kółek. Postaw O!")
        else:
            print("Nie wykonano jeszcze żadnego ruchu. Aby rozpocząć postaw na planszy X lub O")


    def czy_wygrana(self, ostatni_znak: str) -> bool:
        """
        Metoda sprawdza czy stan planszy odpowiada warunkowi wygranej zgodnie z powszechnie obowiązującymi zasadmi gry w kółko i krzyżyk
        :param ostatni_znak: Ostatnio użyty znak
        :return: W przypadku braku wygranej zwrot False (dopusczenie do dalszej gry), a jeśli wygrana, to True
        """
        for i in range (0, self.wielkosc_planszy): # sprawdzenie poziomów
            licznik = 0
            for j in range (0, self.wielkosc_planszy):
                if self.plansza[i][j] == ostatni_znak:
                    licznik += 1
                else:
                    break
                if licznik == self.wielkosc_planszy:
                    return True

        for j in range (0, self.wielkosc_planszy): # sprawdzenie pionów
            licznik = 0
            for i in range (0, self.wielkosc_planszy):
                if self.plansza[i][j] == ostatni_znak:
                    licznik += 1
                else:
                    break
                if licznik == self.wielkosc_planszy:
                    return True

        licznik = 0
        for i in range (0, self.wielkosc_planszy): # sprwadzenie skosu 1:1 2:2 3:3
            for j in range (0, self.wielkosc_planszy):
                if i == j:
                    if self.plansza[i][j] == ostatni_znak:
                        licznik += 1
                    else:
                        break
                if licznik == self.wielkosc_planszy:
                    return True

        licznik = 0
        for i in range (0, self.wielkosc_planszy): #sprwadzanie skosu 1:3 2:2 3:1
            j = -(i + 1)
            if self.plansza[i][j] == ostatni_znak:
                licznik += 1
            else:
                break
            if licznik == self.wielkosc_planszy:
                return True

    def stan_gry(self):
        """
        Sprawdzenie czy gra się toczy dalej lub czy któryś z graczy wygrał
        :return: wartość zgodna z treścią zadania
        """
        if self.czy_wygrana(self.ostatnio_uzyty_znak) != True:
            return 0 #trwa gra
        elif self.ostatnio_uzyty_znak == self.znak_o:
            return 1 #wygrały kółka
        elif self.ostatnio_uzyty_znak == self.znak_x:
            return 2 #wygrały krzyżyki



x = PlanszaXO()
print(x)
x.dodaj_element(1, 2, "X")
print(x)
x.dodaj_element(0, 2, "O")
print(x)
x.dodaj_element(0, 1, "X")
print(x)
x.dodaj_element(1, 1, "O")
print(x)
x.dodaj_element(2, 1, "X")
print(x)
x.dodaj_element(2, 0, "O") # zwracana jest wygrana kółek
print(x)
x.dodaj_element(2, 2, "X") # gra nie pozwala dodać kolejnego X na wygraną planszę
print(x)
