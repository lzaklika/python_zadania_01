"""
### Zadanie 8.3 - zadania na bazie zawodnicy
​
Przygotuj zapytania, który dostarczą odpowiedzi na następujące pytania korzystając z bazy danych `zawodnicy`:
​
1 Obok imion i nazwisk skoczków wypisz ich daty urodzenia w formacie typowym dla języka polskiego, czyli np. “07.02.2006 r.”
2 Wypisz listę zawodników w formacie imię nazwisko (kraj), np. “Adam Małysz (POL)”.
3 FIS dba, aby skoczkowie narciarscy nie byli zbyt szczupli i wymaga, aby ich BMI wynosiło co najmniej 20. Wypisz listę zawodników wraz z informacją czy mają odpowiednią wagę w stosunku do swojego wzrostu (informacja powinna być osobnym polem o wartości typu boolean).
4 Obok imion i nazwisko skoczków wypisz ich BMI z dokładnością do 2 i 3 miejsc po przecinku.
5 Wypisując imiona i nazwiska zamień wielkość liter w nazwiskach, tak by tylko pierwsza litera była wielka.
6 Wypisz listę wszystkich polskich zawodników.
7 Wypisz listę wszystkich trenerów bez podanej daty urodzenia.
8 Wypisz listę zawodników w formacie imię nazwisko (kraj), np. “Adam Małysz (POL)”. Posortuj tę listę po nazwisku zawodnika, w kolejności alfabetycznej.
9 Wypisz listę trenerów posortowanych według daty urodzenia.
10 Wypisz zawodników posortowanych według BMI
11 Wypisz listę zawodników urodzonych w sezonie od listopada do marca.
12 Znajdź trenerów, którzy nie trenują żadnych zawodników.
13 Znajdź trenerów, którzy trenują jakichś zawodników.
14 Znajdź zawodników, którzy nie mają trenera.
15 Znajdź takich zawodników, którzy są starsi od swoich trenerów. Znajdź takich zawodników, którzy są młodsi od swoich trenerów.
16 Podaj wielkości drużyn narodowych.
17 Policz, ilu jest wszystkich zawodników.
18 Podaj listę ekip uporządkowaną według średniego wzrostu zawodników.
19 Sprawdź, jaki jest największy wzrost w poszczególnych krajach.
20 Sprawdź, jaki jest największy wzrost wśród wszystkich.
21 Policz, ilu zawodników urodziło się w poszczególnych kwartałach.
22 Policz, ilu zawodników urodziło się w poszczególnych latach w poszczególnych kwartałach.
23 Policz, jaka jest średnia wielkość ekipy narodowej.
24 Znajdź zawodników wyższych od Małysza.
25 Znajdź zawodników starszych niż Heinz Kuttin.
26 Wypisz zawodników cięższych niż średnia wśród wszystkich.
27 Wypisz zawodników cięższych niż przeciętny zawodnik z Polski.
28 Wypisz zawodników cięższych niż średnia w danej ekipie.

"""

import psycopg2

conn = psycopg2.connect(host="localhost", database="zawodnicy", user="postgres", password="railroad")

cur = conn.cursor()


print(">>> 1. Obok imion i nazwisk skoczków wypisz ich daty urodzenia w formacie typowym dla języka polskiego, czyli np. “07.02.2006 r.”")

cur.execute("select imie, nazwisko, to_char(data_ur, 'DD.MM.YYYY r.') as data_ur_pl from zawodnicy")
results = cur.fetchall()

for row in results:
    print(row)

print("="*30)
print(">>> 2. Wypisz listę zawodników w formacie imię nazwisko (kraj), np. “Adam Małysz (POL)”", end="\n\n")

cur.execute("select imie, nazwisko, kraj from zawodnicy")
results = cur.fetchall()

for row in results:
    print(f"{row[0]} {row[1].capitalize()} ({row[2]})")

print('='*30)

print(f">>> 3. FIS dba, aby skoczkowie narciarscy nie byli zbyt szczupli i wymaga, aby ich BMI wynosiło co najmniej 20.")
print(">>> Wypisz listę zawodników wraz z informacją czy mają odpowiednią wagę w stosunku do swojego wzrostu (informacja powinna być osobnym polem o wartości typu boolean).", end="\n\n")

cur.execute("select imie, nazwisko, wzrost, waga from zawodnicy")
results = cur.fetchall()

for row in results:
    bmi_good = False
    bmi = float(row[3]) / ((float(row[2]) / 100) ** 2)
    if bmi > 20.0:
        bmi_good = True
    print(f"{row[0]} {row[1].capitalize()} - {bmi_good}")

print('='*30)

print(f">>> 4. Obok imion i nazwisko skoczków wypisz ich BMI z dokładnością do 2 i 3 miejsc po przecinku.", end="\n\n")

cur.execute("select imie, nazwisko, wzrost, waga from zawodnicy")
results = cur.fetchall()

for row in results:
    bmi = float(row[3]) / ((float(row[2]) / 100) ** 2)
    print(f"{row[0]} {row[1].capitalize()} - {bmi:.2f}")

print('='*30)

print(f">>> 5. Wypisując imiona i nazwiska zamień wielkość liter w nazwiskach, tak by tylko pierwsza litera była wielka.")

cur.execute("select imie, nazwisko from zawodnicy")
results = cur.fetchall()

for row in results:
    print(f"{row[0]} {row[1].capitalize()}")

print("="*30)

print(f">>> 6. Wypisz listę wszystkich polskich zawodników.")

cur.execute("select imie, nazwisko, kraj from zawodnicy")
results = cur.fetchall()

for row in results:
    if row[2] == "POL":
        print(row)

print("="*30)

print(f">>> 7. Wypisz listę wszystkich trenerów bez podanej daty urodzenia.")

cur.execute("select * from trenerzy")
results = cur.fetchall()

for row in results:
    if row[3] is None:
        print(row)

print("="*30)

print(f">>> 8. Wypisz listę zawodników w formacie imię nazwisko (kraj), np. “Adam Małysz (POL)”. Posortuj tę listę po nazwisku zawodnika, w kolejności alfabetycznej.")

cur.execute("select imie, nazwisko, kraj from zawodnicy order by nazwisko")
results = cur.fetchall()

for row in results:
    print(f"{row[0]} {row[1].capitalize()} ({row[2]})")

print("="*30)

print(">>> 9. Wypisz listę trenerów posortowanych według daty urodzenia.")

cur.execute("select * from trenerzy order by data_ur_t")
results = cur.fetchall()

for row in results:
    print(row)

print("="*30)

print(">>> 10. Wypisz zawodników posortowanych według BMI") # nie działa pętla - przypisuje zawodnikom identyczna wartosc bmi...

cur.execute("ALTER TABLE zawodnicy ADD COLUMN IF NOT EXISTS wskaznik_bmi numeric")
conn.commit()
cur.execute("select * from zawodnicy")
results = cur.fetchall()

for row in results:
    bmi = float(row[6]) / ((float(row[5]) / 100) ** 2)
    bmi_list = [bmi]
    cur.execute("update zawodnicy set wskaznik_bmi = %s", bmi_list) # krzyczał, że chce parametr indeksowalny, to dostał listę

cur.execute("select * from zawodnicy order by wskaznik_bmi")
results = cur.fetchall()

for row in results:
    print(row)
cur.execute("ALTER TABLE zawodnicy DROP COLUMN wskaznik_bmi")
conn.commit()

print("="*30)

print(">>> 11. Wypisz listę zawodników urodzonych w sezonie od listopada do marca.")

cur.execute("select imie, nazwisko, EXTRACT (MONTH FROM data_ur) as miesiac from zawodnicy")
results = cur.fetchall()

for row in results:
    if row[2] >= 11 or row[2] <= 3:
        print(f"{row[0]} {row[1]}")

print("="*30)

print(">>> 12. Znajdź trenerów, którzy nie trenują żadnych zawodników.")

cur.execute("select imie_t, nazwisko_t from trenerzy left join zawodnicy on trenerzy.kraj = zawodnicy.kraj where zawodnicy.kraj is Null")
results = cur.fetchall()

for row in results:
    print(row)

print("="*30)

print(">>> 13. Znajdź trenerów, którzy trenują jakichś zawodników.") # niestety program wypisuje tyle razy nazwisko trenera ilu skoczków on trenuje

cur.execute("select imie_t, nazwisko_t from trenerzy left join zawodnicy on trenerzy.kraj = zawodnicy.kraj where zawodnicy.kraj is not Null")
results = cur.fetchall()

for row in results:
    print(f"{row[0]} {row[1]}")

print("="*30)

print(">>> 14. Znajdź zawodników, którzy nie mają trenera.") # o dziwo wypisuje trenera GER...

cur.execute("select imie, nazwisko from zawodnicy left join trenerzy on zawodnicy.kraj = trenerzy.kraj where trenerzy.kraj is Null")
results = cur.fetchall()

for now in results:
    print(f"{row[0]} {row[1]}")

print("="*30)

print(">>> 15. Znajdź takich zawodników, którzy są starsi od swoich trenerów. Znajdź takich zawodników, którzy są młodsi od swoich trenerów.")

print("Zawodnicy starsi od swoich trenerów:")
cur.execute("select imie, nazwisko from zawodnicy join trenerzy on zawodnicy.kraj = trenerzy.kraj where data_ur > data_ur_t") # wypisuje wszystkich zawodników
results = cur.fetchall()

for row in results:
    print(row)

print("Zawodnicy młodsi od swoich trenerów:")
cur.execute("select imie, nazwisko from zawodnicy join trenerzy on zawodnicy.kraj = trenerzy.kraj where data_ur < data_ur_t")
results = cur.fetchall()

for row in results:
    print(row)

print("="*30)

print(">>> 16. Podaj wielkości drużyn narodowych.")

cur.execute("select kraj, count(*) from zawodnicy group by kraj")
results = cur.fetchall()

for row in results:
    print(f"{row[0]} - {row[1]}")

print("="*30)

print(">>> 17. Policz, ilu jest wszystkich zawodników.")

cur.execute("select * from zawodnicy")
results = cur.fetchall()
count = 0

for row in results:
    count += 1

print(f"Liczba zarejestrowanych zawodników: {count}")

print("="*30)

print(">>> 18. Podaj listę ekip uporządkowaną według średniego wzrostu zawodników.")

cur.execute("select kraj, avg(wzrost) as wzrost_avg from zawodnicy group by kraj order by wzrost_avg")
results = cur.fetchall()

for row in results:
    print(f"{row[0]} - {row[1]:.2f}")

print("="*30)

print(">>> 19. Sprawdź, jaki jest największy wzrost w poszczególnych krajach.")

cur.execute("select kraj, max(wzrost) as wzrost_max from zawodnicy group by kraj order by wzrost_max")
results = cur.fetchall()

for row in results:
    print(f"{row[0]} - {row[1]:.2f}")

print("="*30)

print(">>> 20. Sprawdź, jaki jest największy wzrost wśród wszystkich.")

cur.execute("select max(wzrost) as wzrost_max from zawodnicy kraj order by wzrost_max")
results = cur.fetchall()

for row in results:
    print(f"Wzrost najwyższego zawodnika: {row[0]:.2f}")

print("="*30)

print(">>> 21. Policz, ilu zawodników urodziło się w poszczególnych kwartałach.")

cur.execute("select EXTRACT (MONTH FROM data_ur) as miesiac from zawodnicy")
results = cur.fetchall()
Q_I = 0
Q_II = 0
Q_III = 0
Q_IV = 0

for row in results:
    if row[0] < 4:
        Q_I += 1
    elif row[0] < 7:
        Q_II += 1
    elif row[0] < 10:
        Q_III += 1
    elif row[0] < 13:
        Q_IV += 1

print(f"I kwartał - {Q_I}")
print(f"II kwartał - {Q_II}")
print(f"III kwartał - {Q_III}")
print(f"IV kwartał - {Q_IV}")