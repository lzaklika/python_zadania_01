# ### Zadanie 4.1 | Ogłoszenia
# ​
# Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia
# (takie jak w serwisie internetowym z ogłoszeniami).
# ​
# Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy,
# które posiada każde ogłoszenie, m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.

class Advertisement():
    def __init__(self, title: str, description: str, price: float, currency: str, contact_mail: str, contact_phone: int):
        self.title = title
        self.description = description
        self.price = price
        self.currency = currency
        self.contact_mail = contact_mail
        self.contact_phone = contact_phone

    def __str__(self):
        return f"{self.title} \n\n{self.description} \nCena: {self.price:.2f} {self.currency}\nDANE KONTAKTOWE:\nmail: {self.contact_mail}\ntel.: {self.contact_phone}"

adv1 = Advertisement("Sprzedam Opla", "Opel Astra, przebieg 200 tys. km, czarny, rocznik 1890", 20000, "PLN", "opel@opel.yn", 512345678)
adv2 = Advertisement(price= 1200, currency="JPY", title="Udon", description="Promocja! Makaron Udon w porze lunchowej! Zamów już teraz!", contact_mail="udon@noddle.jp", contact_phone=123123321)
print(adv1)
print(adv2)
