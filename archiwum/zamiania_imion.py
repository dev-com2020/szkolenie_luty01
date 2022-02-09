# imiona = ['Jakub', 'Bartosz', 'Julia', 'Max', 'Agata']
#
# print('Pierwsza wersja listy:', imiona)
# imie = input("Które imię mam zmienić? ")
# imie_index = imiona.index(imie)
# nowe = input('Podaj nowe imię: ')
# imiona[imie_index] = nowe
# print('Druga wersja listy:', imiona)

imiona = ['Jakub', 'Bartosz', 'Julia', 'Max', 'Agata']
zmienna = input("Podaj imię do zmiany: ")
zmienn2 = input("podaj nowe imię: ")

if zmienna in imiona:
    imiona.remove(zmienna)
    imiona.insert(0,str(zmienn2))
print(imiona)
