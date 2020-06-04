"""
Zaimplementuj iterator zwracający jedynie samogłoski z zadanego ciągu znaków:
​
Przykładowe użycie:
for char in Vowels('ala ma kota a kot ma ale'):
    ...

"""

class samogloski:
    def __init__(self, napis: str):
        self.napis = napis

    def __iter__(self):
        self.numer_znaku = 0
        self.samogloski = "aiouey"
        return self

    def __next__(self):

        while self.numer_znaku < len(self.napis):
            znak = self.napis[self.numer_znaku].lower()
            self.numer_znaku += 1

            if znak in self.samogloski:
                return znak

        raise StopIteration

napis = "Ala ma kota a kot ma kompilator"

for znak in samogloski(napis):
    print(znak, end="")

# s = "wrzenie"
# iter = iter(samogloski(s))
# print(next(iter))
# print(next(iter))
# print(next(iter))
#

