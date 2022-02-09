def przywitaj():
    imie = "Tomek"
    return "Cześć!", imie


# imie = "Franek"

# odp = input("Czy mam się przywitać?")
# if odp == "t":
#     print(przywitaj())
# else:
#     print("No dobra, to nara",imie)


def mnozenie(l1, l2):
    # print("Wynik mnożenia: ",l1*l2)
    return l1 * l2


# print(mnozenie(2, 3))

def dodawanie(l1, l2):
    wynik = l1 + l2
    return wynik


# liczba1 = 3
# liczba2 = 4
# wynik = dodawanie(liczba1, liczba2)
# print(wynik)


def ksero(tekst, ile=1):
    print(tekst * ile)


# ksero(ile=5, tekst="Tomek ")


def many_things(*imie, **kwargs):
    # print(args)
    print(imie)
    print(kwargs)


# many_things(liczba=55)

oceny = [3, 4, 5, 6, 3, 1, 1, 4, 4, 6, 6, 6]

import matplotlib.pyplot as plt

def srednia_ocen(oceny):
    if type(oceny) is not list:
        return f'Błędne dane wejściowe! {type(oceny)}'
    suma = sum(oceny)
    if oceny.count(5) > 4 or oceny.count(6) > 4:
        suma += 4
    srednia = sum(oceny) / len(oceny)
    legenda = ["1", "2", "3", "4", "5", "6"]
    oceny_zliczone = [oceny.count(x) for x in range(1, 7)]
    plt.pie(oceny_zliczone, labels=legenda)
    plt.show()
    return round(srednia, 2)


# print(srednia_ocen("A nie ma tutaj ocen"))
print(srednia_ocen(oceny))
