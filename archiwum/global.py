a = 5


def dodawanie():
    global a
    a = 1
    b = 2
    print("Wynik: ", a + b)


def dodaje_tez():
    a = 10
    c = 3
    print("Wynik: ", a + c)


dodawanie()

dodaje_tez()
print("Wartośc a: ", a)
