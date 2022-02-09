import matplotlib.pyplot as plt

oceny = [3, 4, 5, 6, 3, 1, 1, 4, 4, 6, 6, 6]


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


# print("Średnia ocen ucznia to: ", srednia_ocen(oceny))
# input("Wciśnij klawisz ENTER aby zakończyć...")
