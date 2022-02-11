def wykonaj(funkcja, a, b):
    x = funkcja(a, b)
    return x


def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy funkcje")
        return funkcja(*args, **kwargs)

    return wew


@dekor
def zwykla(a, b, c):
    print("To jest zwykła funkcja")
    print(a + b + c)


zwykla(1, 2, 3)

# zmienna = dekor(zwykla)
# print(zmienna)
# zmienna()


print(wykonaj(dodaj, 3, 4))
