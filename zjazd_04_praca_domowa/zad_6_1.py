"""
Plik CSV z danymi: http://pgradzinski.students.alx.pl/kpython/zawodnicy.csv
​
Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:
​
1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)). Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać, być może w innej kolejności:
​
```
AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
```
​
4. jak wyżej, ale liczy jeszcze dla każdego kraju średni wzrost zawodników.
"""

import csv

# file = open("zawodnicy.csv", "r")
# zawartosc = file.read()
# print(zawartosc)
# file.close()
max_height = 0
max_weight = 0
with open('zawodnicy.csv', 'r', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")




    for row in reader:
        # print(row[4])
        # print(max_height)
        if int(row[4]) > max_height:
            max_height = int(row[4])
    print(max_height)
    file.seek(0)

    for row in reader:
        if int(row[4]) == max_height:
            # print(f"{row[0]} {row[1]}")
            print(f"Dane najwyższego skoczka: {row}")
    file.seek(0)

    for row in reader:
        if int(row[5]) > max_weight:
            max_weight = int(row[5])
    print(max_weight)
    file.seek(0)

    for row in reader:
        if int(row[5]) == max_weight:
            print(f"Dane najcięższego skoczka: {row}")
    file.seek(0)

    min_weight = max_weight
    for row in reader:
        if int(row[5]) < min_weight:
            min_weight = int(row[5])
    print(min_weight)
    file.seek(0)

    for row in reader:
        if int(row[5]) == min_weight:
            print(f"Dane najlżejszego skoczka: {row}")
    file.seek(0)


    kraj = "POL"
    suma_wagi = 0
    for row in reader:
        if row[2] == kraj:
            suma_wagi += float(row[5])
    print(f"Sumaryczna waga skoczków z {kraj}: {suma_wagi} kg.")
    file.seek(0)


    country_jumpers_count = {}
    country_jumpers_height_average = {}
    country_list = []
    for row in reader:
        if row[2] not in country_list:
            country_list.append(row[2])
    country_list.sort()
    print(country_list)
    file.seek(0)

    for country in country_list:
        country_jumpers_count[country] = 0
        country_jumpers_height_average[country] = 0
        # print(country_jumpers_count)
        for row in reader:
            if row[2] == country:
                country_jumpers_count[country] += 1
                country_jumpers_height_average[country] += float(row[4])
        file.seek(0)
    print(country_jumpers_count)
    print(country_jumpers_height_average)
    print(country_jumpers_height_average.values())
    # for country, value in country_jumpers_height_average:
    #     country_jumpers_height_average[country].value() / country_jumpers_count[country].value()
    # print(f"Wypisuję {country_jumpers_height_average}")
    for i in country_jumpers_height_average:
        for j in country_jumpers_count:
            if country_jumpers_count.keys() == country_jumpers_height_average.keys():
                country_jumpers_height_average[i] /= country_jumpers_count[j]
    print(country_jumpers_height_average)
