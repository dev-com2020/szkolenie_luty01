# lambda param : wyrażenie

dodaj = lambda x, y, z: x + y - z


# print(dodaj(2, 3, 1))


# def funkcja(x):
#     x + 1
#
# lambda x: x + 1

def funkcja(f, liczba):
    return f(liczba)


# def dodaj_jeden(x):
#     return x + 1
#
#
# def kwadrat(par):
#     return par * par

# print(funkcja(lambda x: x + 1, 7))
# print(funkcja(lambda x: x * x, 7))

# print(funkcja(dodaj_jeden, 7))
# print(funkcja(kwadrat, 7))

from functools import reduce


# lista = [1, 3, 5, 7]
# print(f"Nasza lista:{lista}")
# print(f"Zastosowanie map na liście: {list(map(lambda _:_*2,lista))}")
# print(f"Zastosowanie filter na liście: {list(filter(lambda _:_>3,lista))}")
# print(f"Zastosowanie reduce na liście: {reduce(lambda x,y: x+y,lista)}")

def my_func(n):
    return n * (n - 1)


number = [1, 5, 12, 30]
z_funk = list(map(my_func, number))
z_lamb = list(map(lambda a: a * (a - 1), number))

print(z_funk)
print(z_lamb)

slownik = {'a': 11, 'b': 2, 'c': 0, 'd': 33}

print(sorted(slownik))
print(sorted(slownik.values()))
print(sorted(slownik.items()))

print(sorted(slownik.items(), key=lambda x: x[1]))