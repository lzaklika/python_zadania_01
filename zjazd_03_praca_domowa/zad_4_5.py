# ### Zadanie 4.5 | Żółw
# ​
# Napisz klasę `Zolw` z metodami `idz` i `obroc_sie`.
# Żółw ma jakieś położenie (wyrażone dwiema współrzędnymi) i jakieś ustawienie,
# czyli kurs (wyznaczony pojedyncza liczba).
# ​
# Początkowe położenie podajemy konstruktorowi klasy, początkowy kurs to zawsze 0.
# ​
# Metoda `obroc_sie ` powoduje obrót żółwia, czyli zmianę jego kursu.
# ​
# Metoda `idz` powoduje przejście żółwia o określoną odległość.
# ​
# Z klasy będzie się korzystać tak:
# ​
# ```python
# z = Zolw(100, 100)
# z.idz(50)
# ​
# print(z) # ma sie wypisac: x=100, y=50
# ​
# z.obroc_sie(90)
# z.idz(50)
# ​
# print(z) # ma sie wypisac: x=150, y=50
# ```
import math


class Zolw():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.kurs = 0


    # def obroc_sie(self, obrot: int) -> int:
    #     if obrot == -270 or obrot == -180 or obrot == -90 or obrot == 0 or obrot == 90 or obrot == 180 or obrot == 270:
    #
    #         if self.kurs + obrot >= 360:
    #             obrot -= 360
    #         elif self.kurs + obrot <= -360:
    #             obrot += 360
    #         else:
    #             self.kurs += obrot
    #
    #     else:
    #         raise ValueError("Ten żółw umie obracać się jedynie o kąt prosty!")
    #         return
    #
    #     return self.kurs

    def obroc_sie(self, obrot: int) -> int:
        if obrot % 90 == 0:

            if self.kurs + obrot >= 360:
                ile = math.floor((self.kurs + obrot) / 360)
                self.kurs = (self.kurs + obrot) - (ile * 360)
            elif self.kurs + obrot <= -360:
                ile = math.ceil((self.kurs + obrot) / 360)
                self.kurs = (self.kurs + obrot) - (ile * 360)
            else:
                self.kurs += obrot

        else:
            raise ValueError("Ten żółw umie obracać się jedynie o kąt prosty!")
            return

        return self.kurs

    def idz(self, dystans: int):
        if self.kurs == 0 or self.kurs == -360:
            self.y -= dystans
        elif self.kurs == 90 or self.kurs == -270:
            self.x += dystans
        elif self.kurs == 180 or self.kurs == -180:
            self.y += dystans
        elif self.kurs == 270 or self.kurs == -90:
            self.x -= dystans
        else:
            print("Ten komunikat nie powinien się wyświetlić! Coś poszło nie tak...")


    def __str__(self) -> str:
        return f"x={self.x}, y={self.y}"


z = Zolw(100, 100)
print(z)

z.idz(50)
print(z)

z.obroc_sie(-90)
z.idz(50)
print(z)

z.obroc_sie(-180)
z.idz(50)
print(z)

z.obroc_sie(-180)
z.idz(25)
print(z)
