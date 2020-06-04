"""
Zaimplementuj generator zwracający jedynie samogłoski z zadanego ciągu znaków:
​
Przykładowe użycie:
for char in vowels('ala ma kota a kot ma ale'):
    ...

"""

def samogloski(napis: str):
    for znak in napis:
        if znak.lower() in "aiouey":
            yield znak

napis = "Ala ma kota a kot ma kompilator"
for znak in samogloski(napis):
    print(znak, end="")


