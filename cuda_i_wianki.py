# -*- coding: utf-8 -*-
"""cuda_i_wianki.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F7XFdYQ1ZzCyrrQhjxpybKcyvO8oW0Q_
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Moja lista=",lista)
# print("Suma liczb z listy: ",sum(lista))
imie = "tomek"
# print(imie.upper())
slownik = {1 : "jeden",
           2: "dwa",
           "trzy" : 3,
           4 : {"a": 100, "b": 200},
           5: [1,2,3]}

# print(slownik[5])
# print(slownik.keys())
# print(slownik.values())
# print(1 in slownik.keys())
# print(1 in slownik)
slownik[2] = "Tomek"
# print(slownik[2])

krotka = (1,2,"Adam",3.4)
# print(krotka[2:4])
lista_z_krotki = list(krotka)
# print(lista_z_krotki)

x = 1,2,3
# print(x)
x1,x2,x3 = x
# print(x1,x2)

oceny = {1,2,3,4,5,6,3,5}
oceny2 = {1,1,2,3,7,8,9}
# print(oceny - oceny2)
# print(oceny.difference(oceny2))
# print(oceny & oceny2)
# print(oceny.intersection(oceny2))
# print(oceny | oceny2)

# print(oceny)
# print(oceny2)

# liczby = list(range(1,10,2))
# print(liczby)

# liczby2 = list(range(-5,-10,-2))
# print(liczby2)

# import random

# kosc6 = random.randint(1,6)
# print("Wylosowana liczba na kości to: ", kosc6)

# wyniki = []

# for i in range(3):
#     print("Pętla nr: ",i+1)
#     wyniki.append(100 * i+1)

# print(wyniki)

# lista = [4,5,6]
# for index, wartosc in enumerate(lista):
#     print(str(index) + " --> " + str(wartosc))


# slownik = {"imie": "Marek", "nazwisko": "Kowalski", "plec": "mezczyzna"}

# for key in slownik:
#     print(key)

# for val in slownik.values():
#     print(val)

# for key,value in slownik.items():
#     print(key + " ==> " + value)

licznik = 0
while licznik < 5:
    print(str(licznik) + " mniejsze od 5")